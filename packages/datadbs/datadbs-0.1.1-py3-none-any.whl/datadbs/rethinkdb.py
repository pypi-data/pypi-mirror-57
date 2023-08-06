from rethinkdb import RethinkDB as rdb
import asyncio
from typing import Callable, Dict
from datetime import datetime, timezone
import logging

from pathlib import Path
import os
import time

from .general import GeneralData
from networktools.colorprint import gprint, bprint, rprint


class Rethink_DBS(GeneralData):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.station = self.code
        self.default_db = ''
        self.dbname = kwargs.get('dbname')
        self.loop = None
        if 'io_loop' in kwargs.keys():
            self.loop = kwargs['io_loop']
            asyncio.set_event_loop(self.loop)
        self.env = kwargs.get('env', 'natural')
        self.dblist = []
        self.tables = {}
        self.index = {}
        time.sleep(1)
        self.set_defaultdb(self.dbname)
        r = rdb()
        r.set_loop_type('asyncio')
        self.r = r

    async def msg_log(self, msg, level):
        if self:
            self.save_log(msg, level)

    async def async_connect(self, loop=None):
        self.session = None
        try:
            if self.default_db:
                kwargs = {}
                if not loop:
                    kwargs = {'io_loop': loop}
                else:
                    kwargs = {'io_loop': self.loop}
                dbname = self.dbname
                dbhost = self.address[0]
                dbport = self.address[1]
                self.session = await self.r.connect(
                    db=dbname,
                    host=dbhost, **kwargs)
                self.logger.info(
                    "Connected to RethinkDB with database %s" % self.default_db)
            else:
                self.session = await self.r.connect(host=self.address[0])
                print("Aún no se selecciona database")
                self.logger.info(
                    "Connected to RethinkDB without database selected")
        except Exception as ex:
            print("Excepcion al conectar a Rethinkdb %s" % ex)
            raise ex
        return self.session

    def close(self):
        self.session.close(noreply_wait=False)

    async def reconnect(self, wait=False):
        await self.session.reconnect(noreply_wait=wait)

    # database manage
    def set_defaultdb(self, dbname: str):
        self.default_db = dbname
        self.logger.info("Database set on %s by default" % dbname)

    async def server_info(self):
        self.logger.info("Info from server obtained")
        return await self.session.server()

    async def select_db(self, dbname: str = None):
        if dbname is None:
            # print(self.session)
            result = self.session.use(self.default_db)
            self.logger.info("Set default db to use on session")
        else:
            result = await self.list_dbs()
            if dbname in self.dblist:
                result = self.session.use(dbname)
                self.set_defaultdb(dbname)
                self.logger.info("Set db to use on session")
            else:
                self.logger.error(
                    "Set default db to use on session, and database doesn\'t exists")
                print(
                    "There are no database with name %s, so we create that" % dbname)
                await self.create_db(dbname)
        return result

    async def create_db(self, dbname: str = None):
        try:
            if dbname == None:
                dbname = self.default_db
            await self.list_dbs()
            if dbname not in self.dblist:
                self.set_defaultdb(dbname)
                result = await self.r.db_create(self.default_db).run(self.session)
                self.logger.info("Database %s creada" % dbname)
            else:
                result = "Database exists"
        except Exception as exec:
            print("An exception happen when try to create a database: %s" % exec)
            raise exec
        return result

    async def delete_db(self, dbname: str):
        self.logger.info("Delete database %s" % dbname)
        return await self.r.db_drop(dbname).run(self.session)

    async def list_dbs(self):
        self.logger.info("Lists databases on %s" % self.hostname)

        self.dblist = await self.r.db_list().run(self.session)
        # print("Lista de databasesx")
        return self.dblist

    # table manager

    async def create_table(self, table_name: str, dbname: str = None):
        self.logger.info("Creating table %s" % table_name)
        if dbname == None:
            dbname = self.default_db
        try:
            await self.list_tables(self.default_db)
            # print("Tables by database: %s" %self.tables)
            if dbname in self.tables.keys():
                # print("Inside create tables")
                if not table_name in self.tables[dbname]:
                    self.logger.info("Creating table named %s" % table_name)

                    return await self.r.db(dbname).table_create(table_name).run(self.session)
                else:
                    self.logger.error("Table exists %s" % table_name)
                    msg = "Table Name %s exists" % table_name
                    # print(msg)
                    return {'msg': msg}
        except Exception as exec:
            self.logger.critical(
                "Error crítico al crear tabla %s" % table_name)
            print("Error al crear table %s" % exec)
            raise exec

    async def get_indexes(self, table_name: str, dbname: str = None):
        if dbname is None:
            dbname = self.default_db
        if table_name in self.tables.get(self.dbname, {}):
            indexes = await self.r.db(dbname).table(table_name).index_list().run(self.session)
            # print("Indexes: %s" %indexes)
            self.index.update({table_name: indexes})
        self.logger.info("Obtaining list of indexes")
        return self.index

    async def create_index(self, table_name: str, index: str = None, dbname: str = None):
        self.logger.info("Creating index %s on table %s" % (index, table_name))
        if dbname is None:
            dbname = self.default_db
        try:
            indexes = []
            if table_name in self.tables.get(self.dbname, {}):
                indexes = await self.r.db(dbname).table(table_name).index_list().run(self.session)
                if not table_name in self.index.keys():
                    self.index.update({table_name: []})

                if not index in indexes:
                    await self.r.db(dbname).table(table_name).index_create(index).run(self.session)
                    await self.r.db(dbname).table(table_name).index_wait().run(self.session)
                    self.index[table_name].append(index)
            else:
                await self.create_table(table_name, dbname)

        except Exception as exec:
            self.logger.critical(
                "Index %s can't be created %s" % (index, table_name))
            print("Error al crear index %s" % exec)
            raise exec

    async def delete_table(self, table_name: str, dbname: str):
        if dbname in self.dblist:
            if table_name in self.tables[dbname]:
                self.logger.info("Table deleted %s on database %s" %
                                 (table_name, dbname))
                return await self.r.db(dbname).table_drop(table_name).run(self.session)

    async def list_tables(self, dbname: str = None):
        tlist = []
        if dbname == None:
            dbname = self.default_db

        await self.list_dbs()
        # print("DB %s in list %s" %(dbname, await self.list_dbs()))
        if dbname in self.dblist:
            tlist = await self.r.db(dbname).table_list().run(self.session)
            # print("Tables on database %s are %s" %(dbname, tlist))
            self.tables.update(
                {dbname: tlist})
            # print(self.tables)
        self.logger.info("Tables listed on database %s" % dbname)

    async def set_change_handler(self, table_name: str):
        changes = await self.r.table(table_name).changes().run(self.session)
        return changes

    async def save_data(self, table_name, data, options=None):
        # print(self.tables)
        try:
            if table_name in self.tables[self.default_db]:
                # print("Sending data %s" %data)
                if options is None:
                    options = {'durability': 'soft', 'return_changes': False}
                return await self.r.table(table_name).insert(data, **options).run(self.session, **options)
        except Exception as ex:
            self.logger.critical(
                "Error in saving data on %s with data %s" % (table_name, data))
            print("Error when send data %s" % exec)
            raise ex

    async def update_data(self, table_name, id, conditional_data):
        self.logger.info("Updating data in %s" % table_name)
        if table_name in self.tables[self.default_db]:
            await self.r.table(table_name).get(id).update(conditional_data).run(self.session)

    async def replace_data(self, table_name, id, conditional_data):
        self.logger.info("Replacing data in %s" % table_name)
        if table_name in self.tables[self.default_db]:
            await self.r.table(table_name).get(id).replace(conditional_data).run(self.session)

    async def delete_data(self, table_name, id):
        self.logger.info("Deleting data in %s" % table_name)
        if table_name in self.tables[self.default_db]:
            if isinstance(id, dict):
                await self.r.table(table_name).filter(id).delete().run(self.session)
            else:
                await self.r.table(table_name).get(id).delete().run(self.session)

    async def get_infoserver(self):
        self.logger.info("Get info server")
        return await self.session.server()

    async def get_data_between(self, table_name, lower, upper):
        self.logger.info("Extracting data between %s and %s from %s" %
                         (lower, upper, table_name))
        if table_name in self.tables[self.default_db]:
            return await self.r.table(table_name).between(lower, upper).run(self.session)
        else:
            print("No hay datos entre esos valores")

    async def get_data(self, table_name, index_name, value):
        return await self.r.table(table_name).get_all(value, index=index_name).run(self.session)

    async def get_data_filter(self,
                              table_name,
                              filter_exp,
                              filter_opt,
                              order_by: str,
                              options={}):
        """
        filter expression could ve a json like:
        {'age':30} or an expression:
        r.row['age']=30 or a lambda function:
        lambda user: user['age]==30
        """
        index = None
        if "index" in filter_opt.keys():
            index = filter_opt["index"]
            if not index:
                index = None
        if table_name in self.tables.get(self.default_db, {}):
            options = {'read_mode': 'single'}

        try:
            if table_name in self.tables.get(self.default_db, {}):
                if index:
                    # print("Between")
                    lower = None
                    upper = None
                    if not type(filter_exp) == list:
                        lower = filter_exp
                        upper = self.r.maxval
                    else:
                        lower = filter_exp[0]
                        upper = filter_exp[1]
                    self.logger.info("Obtaining data from %s to %s on table %s, with filters %s using index %s" % (lower,
                                                                                                                   upper,
                                                                                                                   table_name,
                                                                                                                   filter_opt,
                                                                                                                   index))
                    return await self.r.table(table_name).between(lower, upper,
                                                                  **filter_opt).order_by(
                        order_by).run(self.session,
                                      **options)
                else:
                    self.logger.info("Obtaining data with filters %s using table %s" % (
                        filter_opt, table_name))

                    return await self.r.table(table_name).filter(
                        filter_exp).order_by(
                        order_by).run(
                        self.session, **options)
            else:
                return []
        except Exception as ec:
            self.logger.critical("Error on the data extraction")
            print("Error en consulta de datos %s -> %s" % (self, ec))
            await asyncio.sleep(60)
            await self.reconnect(wait=True)
            raise ec

    def iso8601(self, date):
        return self.r.iso8601(date)

    def loginfo(self, msg):
        self.logger.info(msg)

    def logdebug(self, msg):
        self.logger.debug(msg)

    def logerror(self, msg):
        self.logger.error(msg)

    # DEFINE JOINS....
    # https://www.rethinkdb.com/api/python/#index_create
