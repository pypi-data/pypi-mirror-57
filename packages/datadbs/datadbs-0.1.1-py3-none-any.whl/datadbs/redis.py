import time
from datetime import datetime
import os
try:
    from .general import GeneralData
except:
    from .general import GeneralData

import pickle
import redis

from networktools.time import timestamp
from networktools.colorprint import rprint, bprint, gprint

import struct

import asyncio
import asyncio_redis

def double_unpack(value):
    return struct.unpack('d',value)[0]

def load_data(data):
    return (pickle.loads(data[0]), data[1])

class RedisData(GeneralData):

    def __init__(self,**kwargs):
        super(RedisData, self).__init__()
        self.host=kwargs['host']
        self.port=kwargs['port']
        self.name=kwargs['name']
        if 'poolsize' in kwargs.keys():
            self.poolsize=kwargs['poolsize']
        self.user=kwargs['user']
        self.passw=kwargs['passw']
        self.station=kwargs['code']
        self.time_format ="%Y%m%d_%H%M%S"
        self.session=None#redis.StrictRedis(host=self.host, port=self.port)
        self.list_keys=[]
        print("Sesion REDIS ok %s" %self.station)

    def connect(self):
        self.session=redis.StrictRedis(host=self.host, port=self.port)

    async def async_connect(self):
        self.session=await asyncio_redis.Connection.create(host=self.host, port=self.port, poolsize=self.poolsize)

    def set_station(self,station):
        self.station=station

    def save_data(self, data):
        #Data is a dict with the tuples for some tables
        #STATION={table1={timestamp=value,values=xxx}, table2={timestamp=value, values=axasdasda}}
        print(data)
        print("Save on database REDIS %s" % data)
        station=self.station
        session=self.session
        before=dict()
        i=0
        ts=0
        try:
            #Clean timestamp register on data dict
            #print(data.keys())
            for table in data.keys():
                if i==0:
                    this_dt=data[table]['TIMESTAMP']
                    #in_dtformat=datetime.strptime(this_dt, self.time_format)
                    ts=this_dt*1e6
                    #print("Timestamp %s " %ts)
                    #ts=struct.pack('d',in_dtformat.timestamp())
                    i+=1
                #print(ts)
                #drop timestamp info from data
                data[table].pop('TIMESTAMP', None)
                    #list
            to_save=pickle.dumps(data)
            try:
                session.zadd(station, ts, to_save)
            except Exception as exec:
                print("Falla al hacer zadd" % exec)
                raise exec
        except Exception as exec:
            print(exec)
            raise exec


    def get_stamps(self):
        mkeys=self.session.hkeys(self.station)
        list_keys=list(map(double_unpack,mkeys))
        self.list_keys=list_keys

    def zcard(self):
        return self.session.zcard(self.station)

    def gsize(self):
        return self.zcard()

    def get_data(self, n0,nf):
        station=self.station
        #pool map?
        bprint("Almost gettings data from %s station" % station)
        rprint(self.session)
        query=self.session.zrange(station, n0, nf, withscores=True)
        return query

    def filter_data(self, query, tables, columns):
        query_filtered=dict()
        for ts in query.keys():
            query_filtered[ts]=dict()
            for t in tables:
                data_table=query[ts][t]
                table_filtered=dict()
                for c in columns:
                    if c in data_table.keys():
                        table_filtered[c]=data_table[c]
                query_filtered[ts][t]=table_filtered
        return query_filtered

    def get_rt_data(self, z0):
        if not self.session:
            self.session=redis.StrictRedis(host=self.host, port=self.port)
        #rprint("Almost z0 : %s" % z0)
        zcard=self.zcard()
        #bprint("Almost new zcard %s" % zcard)
        query=self.get_data(z0, zcard)
        #bprint("Almost query %s %s" % (len(query), type(query) ))
        values=list(map(load_data,query))
        #gprint("Almost new values %s" % format(values))
        return values, zcard


