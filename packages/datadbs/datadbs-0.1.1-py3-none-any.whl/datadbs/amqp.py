from networktools.geo import (rad2deg, deg2rad, radius, sph_rotation_matrix,
                              llh2ecef, ecef2llh, ecef2neu)
from networktools.time import timestamp, gps_week2time, gps_time
from networktools.statistics import matrix_VCV, rotate
from .geojson import GeoJSONData
import json
import pika
import copy
from networktools.colorprint import gprint, bprint, rprint
import asyncio
from .general import GeneralData
from io import StringIO
from tasktools.taskloop import coromask, renew, simple_fargs, simple_fargs_out
import functools as fc


class AMQPData(GeneralData):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.creds = kwargs.get('credentials', [])
        self.vhost = kwargs.get('vhost', '/')
        self.exchange = kwargs.get('exchange', '')
        self.exch_type = kwargs.get('exchange_type', 'fanout')
        self.queue_name = kwargs.get('queue_name', 'status_gnss')
        self.routing_key = kwargs.get('routing_key', 'status')
        self.consumer_tag = kwargs.get('consumer_tag', 'gnss')
        self.durable = kwargs.get('durable', True)
        self.ping = kwargs.get('ping', 30)
        self.connect()

    def connect(self):
        self.credentials = pika.PlainCredentials(*self.creds)
        self.parameters = pika.ConnectionParameters(
            host=self.host,
            virtual_host=self.vhost,
            credentials=self.credentials,
            heartbeat=self.ping)
        self.connection = pika.BlockingConnection(self.parameters)
        self.channel = self.connection.channel()
        self.connected = True
        try:
            self.channel.queue_declare(self.queue_name, durable=self.durable)
        except Exception as e:
            rprint("Error declaring queue -> %s" % e)
            self.connected = False
            raise e

    def reconnect(self):
        """Will be invoked if the connection can't be opened or is
        closed. Indicates that a reconnect is necessary then stops the
        ioloop.
        """
        self.should_reconnect = True
        self.stop()

    def manage_data(self, geojson):
        value = copy.deepcopy(geojson)
        if 'DT_GEN' in value['properties'].keys():
            del value['properties']['DT_GEN']
        if 'dt' in value['properties'].keys():
            del value['properties']['dt']
        text = json.dumps(value)
        res = self.publish(self.exchange, self.routing_key,
                           "{}\n".format(text))
        del value
        return geojson

    def manage_json_data(self, value):
        text = json.dumps(value)
        res = self.publish(self.exchange, self.routing_key,
                           "{}\n".format(text))
        return value

    def send2gui(self, to_gui):
        try:
            text = json.dumps(to_gui)
            res = self.publish(self.exchange,
                               self.routing_key,
                               "{}\n".format(to_gui))
            return res
        except Exception as e:
            gprint("WW error %s" % to_gui)
            raise e

    def publish(self, exchange, key, msg):
        sended = False
        while not sended:
            try:
                self.channel.basic_publish(exchange=exchange,
                                           routing_key=self.routing_key,
                                           body=msg)
                sended = True
            except Exception as e:
                self.connected = False
                print("Fail to send %s" % e)
                self.connect()

    def read_from_gui(self):
        data = []
        count = 0
        for method_frame, properties, body in self.channel.consume(
                self.queue_name):
            try:
                strb = str(body, 'utf-8').replace("'", "\"")
                new_json = json.loads(strb)
            except Exception as e:
                gprint("WW error on loads %s" % body)
                raise e
            data.append(new_json)
            self.channel.basic_ack(method_frame.delivery_tag)
            count += 1
            if count >= 24:
                break
        return data

    async def consume_mq(self, *args):
        queue = args[0]
        active = args[1]
        count = 0
        consumer_args = self.get_consumer_args()
        for method_frame, properties, body in self.channel.consume(
                *consumer_args):
            try:
                strb = str(body, 'utf-8').replace("'", "\"")
                new_json = json.loads(strb)
            except Exception as e:
                gprint("WW error on consume_mq %s" % body)
                raise e
            if active:
                queue.put(new_json)
            else:
                bprint("New data from queue")
                rprint(new_json)
            # self.channel.basic_ack(method_frame.delivery_tag)
            count += 1
            if count >= 24:
                break
        return args

    def get_consumer_args(self):
        return [self.queue_name, self.consumer_tag]

    async def consume_exchange_mq(self, *args):
        queue = args[0]
        active = args[1]
        count = 0
        consumer_args = self.get_consumer_args()
        for method_frame, properties, body in self.channel.consume(
                *consumer_args):
            try:
                strb = str(body, 'utf-8').replace("'", "\"")
                new_json = json.loads(strb)
            except Exception as e:
                gprint("WW error on consume_mq convert json %s" % body)
                raise e
            if active:
                queue.put(new_json)
            else:
                bprint("New data from queue")
                rprint(new_json)
            # self.channel.basic_ack(method_frame.delivery_tag)
            count += 1
            if count >= 1:
                break
        return args

    def create_task(self, queue_mq2ws, active):
        loop = asyncio.get_event_loop()
        args = [queue_mq2ws, active]
        coroutine_future = coromask(self.consume_mq, args, simple_fargs)
        task = loop.create_task(coroutine_future)
        task.add_done_callback(
            fc.partial(renew, task, self.consume_mq, simple_fargs))
        return loop, task

    def create_exchange_task(self, queue_mq2ws, active):
        loop = asyncio.get_event_loop()
        args = [queue_mq2ws, active]
        coroutine_future = coromask(
            self.consume_exchange_mq, args, simple_fargs)
        task = loop.create_task(coroutine_future)
        task.add_done_callback(
            fc.partial(renew, task, self.consume_exchange_mq, simple_fargs))
        return loop, task

    def consume_mq_task(self, queue_mq2ws, active):
        loop, task = self.create_task(queue_mq2ws, active)
        if not loop.is_running():
            loop.run_forever()
