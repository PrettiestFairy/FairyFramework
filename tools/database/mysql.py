# coding: utf8
""" 
@File: mysql.py
@Editor: PyCharm
@Author: Austin (From Chengdu.China) https://fairy.host
@HomePage: https://github.com/AustinFairyland
@OperatingSystem: Windows 11 Professional Workstation 23H2 Canary Channel
@CreatedTime: 2023-10-12
"""
from __future__ import annotations

import sys
import warnings
import platform
import asyncio

sys.dont_write_bytecode = True
warnings.filterwarnings("ignore")
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import random
import pymysql

from modules.inheritance import Base
from tools.abnormal import MySQLSourceError
from tools.abnormal import ParamsError


class MySQLStandaloneToolsClass(Base):
    """MySQL Single Node Database"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __mysql_config(self) -> dict:
        try:
            config = self.config.get("datasource").get("mysql").get("standalone")
        except Exception as error:
            self.exception(error)
            sys.exit(1)
        return config

    def __connect_tool(self):
        """
        MySQL Connections
        :return: Connection object: MySQL Connect Object
        """
        try:
            mysql_config = self.__mysql_config()
            if mysql_config is None:
                raise MySQLSourceError("MySQL Source Configuration Error.")
            __host = mysql_config.get("host")
            __port = mysql_config.get("port")
            __user = mysql_config.get("user")
            __password = mysql_config.get("password")
            __database = mysql_config.get("database")
            __charset = mysql_config.get("charset")
            if __charset is None:
                __charset = "utf8mb4"
            if not all((__host, __port, __user, __password, __database)):
                raise MySQLSourceError("MySQL Source Configuration Error.")
            self.debug("MySQL Standalone IP：{}".format(__host))
            self.debug("MySQL Standalone Port：{}".format(__port))
            self.debug("MySQL Standalone User：{}".format(__user))
            self.debug("MySQL Standalone Database：{}".format(__database))
            self.debug("MySQL Standalone Charset：{}".format(__charset))
            connect = pymysql.connect(
                host=__host,
                port=__port,
                user=__user,
                password=__password,
                database=__database,
                charset=__charset,
                connect_timeout=5,
            )
            self.info("MySQL Connection Successful.")
            return connect
        except Exception as error:
            # self.exception(error)
            self.error(error)
            sys.exit(1)

    def query(self, query: str):
        """
        MySQL Data Queries
        :param query: SQL query statements: String
        :return: results: Iteratable Object
        """
        self.debug("MySQL Data Queries")
        conn = self.__connect_tool()
        cur = conn.cursor()
        try:
            self.info("SQL - {}".format(query))
            cur.execute(query=query)
            result = cur.fetchall()
            self.info("Results - {}".format(result))
            conn.commit()
        except Exception as error:
            result = None
            conn.rollback()
            self.debug("Successful execution of query transaction：{}".format(query))
            self.error(error)
            # self.exception(error)
        finally:
            cur.close()
            conn.cursor()
        return result

    def __operation(self, query: str):
        """
        Private methods execute SQL statements that do not return query data.
        :param query: SQL query statements: String
        :return: Ture or False: Boolean
        """
        conn = self.__connect_tool()
        cur = conn.cursor()
        try:
            cur.execute(query=query)
            conn.commit()
            self.debug("MySQL Transaction Executed Successfully：{}".format(query))
            result = True
        except Exception as error:
            conn.rollback()
            self.error("MySQL Transaction Execution Failure：{}".format(query))
            self.exception(error)
            result = False
        finally:
            cur.close()
            conn.close()
        return result

    def operation(self, query: str):
        """
        The executed SQL statement does not return query data.
        :param query: SQL query statements: String
        :return: Ture or False: Boolean
        """
        self.debug("MySQL Operations")
        return self.__operation(query=query)

    def insert(self, query: str):
        """
        Inserting SQL Data
        :param query: SQL query statements: String
        :return: Ture or False: Boolean
        """
        self.debug("MySQL Data Insert")
        return self.__operation(query=query)

    def update(self, query: str):
        """
        Updating SQL Data
        :param query: SQL query statements: String
        :return: Ture or False: Boolean
        """
        self.debug("MySQL Data Updates")
        return self.__operation(query=query)

    def delete(self, query: str):
        """
        Delete SQL Data
        :param query: SQL query statements: String
        :return: Ture or False: Boolean
        """
        self.debug("MySQL Data Deletion")
        return self.__operation(query=query)


class MySQLMasterSlaveDBRouterToolsClass(Base):
    """MySQL Database Read/Write Separation"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def __mysql_config(self) -> dict:
        try:
            config = self.config.get("datasource").get("mysql").get("dbrouter")
        except Exception as error:
            self.exception(error)
            sys.exit(1)
        return config

    def __mysql_master_config(self) -> dict:
        """
        Getting Master Configuration Information
        :return: Master Configuration Information: Dict
        """
        try:
            mysql_config_master: list = self.__mysql_config.get("master")
            return random.choice(mysql_config_master)
        except Exception as error:
            self.exception(error)
            sys.exit(1)

    def __mysql_slave_config(self) -> dict:
        """
        Getting Slave Configuration Information
        :return: Slave Configuration Information: Dict
        """
        try:
            mysql_config_slave: list = self.__mysql_config.get("slave")
            return random.choice(mysql_config_slave)
        except Exception as error:
            self.exception(error)
            sys.exit(1)

    @property
    def __connect_master_tool(self):
        """
        MySQL Master Connection
        :return: Connection object: MySQL Connect Object
        """
        try:
            __master_config = self.__mysql_master_config()
            __master_host = __master_config.get("host")
            __master_port = __master_config.get("port")
            __master_user = __master_config.get("user")
            __master_password = __master_config.get("password")
            __master_database = __master_config.get("database")
            __master_charset = __master_config.get("charset")
            if not __master_charset:
                __master_charset = "utf8mb4"
            if not all(
                (
                    __master_host,
                    __master_port,
                    __master_user,
                    __master_password,
                    __master_database,
                )
            ):
                raise MySQLSourceError("MySQL Master Configuration Error")
            self.debug("MySQL Data Source：MySQL Master DBRouter")
            self.debug("MySQL Master DBRouter IP：{}".format(__master_host))
            self.debug("MySQL Master DBRouter Port：{}".format(__master_port))
            self.debug("MySQL Master DBRouter Username：{}".format(__master_user))
            self.debug("MySQL Master DBRouter Database：{}".format(__master_database))
            self.debug("MySQL Master DBRouter Charset：{}".format(__master_charset))
            connect = pymysql.connect(
                host=__master_host,
                port=__master_port,
                user=__master_user,
                password=__master_password,
                database=__master_database,
                charset=__master_charset,
            )
            return connect
        except Exception as error:
            self.exception(error)
            sys.exit(1)

    @property
    def __connect_slave_tool(self):
        """
        MySQL Slave Connection
        :return: Connection object: MySQL Connect Object
        """
        try:
            __slave_config = self.__mysql_slave_config()
            __slave_host = __slave_config.get("host")
            __slave_port = __slave_config.get("port")
            __slave_user = __slave_config.get("user")
            __slave_password = __slave_config.get("password")
            __slave_database = __slave_config.get("database")
            __slave_charset = __slave_config.get("charset")
            if __slave_charset is None:
                __slave_charset = "utf8mb4"
            if not all(
                (
                    __slave_host,
                    __slave_port,
                    __slave_user,
                    __slave_password,
                    __slave_database,
                )
            ):
                raise MySQLSourceError("MySQL Slave Configuration Error")
            self.debug("MySQL Data Source：MySQL Slave DBRouter")
            self.debug("MySQL Slave DBRouter IP：{}".format(__slave_host))
            self.debug("MySQL Slave DBRouter Port：{}".format(__slave_port))
            self.debug("MySQL Slave DBRouter Username：{}".format(__slave_user))
            self.debug("MySQL Slave DBRouter Database：{}".format(__slave_database))
            self.debug("MySQL Slave DBRouter Charset：{}".format(__slave_charset))
            connect = pymysql.connect(
                host=__slave_host,
                port=__slave_port,
                user=__slave_user,
                password=__slave_password,
                database=__slave_database,
                charset=__slave_charset,
            )
            return connect
        except Exception as error:
            self.exception(error)
            sys.exit(1)

    def query(self, query: str):
        """
        MySQL Data Queries
        :param query: SQL query statements: String
        :return: results: Iteratable Object
        """
        self.debug("MySQL Data Queries")
        conn = self.__connect_slave_tool
        cur = conn.cursor()
        try:
            cur.execute(query=query)
            result = cur.fetchall()
            conn.commit()
        except Exception as error:
            result = None
            conn.rollback()
            self.exception(error)
        finally:
            cur.close()
            conn.close()
        return result

    def inster(self, query: str):
        """
        Insert SQL Data
        :param query: SQL query statements: String
        :return: True or False: Boolean
        """
        self.debug("MySQL Data Insertion")
        return self.master_operation(query=query)

    def update(self, query: str):
        """
        Update SQL Data
        :param query: SQL query statements: String
        :return: True or False: Boolean
        """
        self.debug("MySQL Data Updates")
        return self.master_operation(query=query)

    def delete(self, query: str):
        """
        Delete SQL Data
        :param query: SQL query statements: String
        :return: True or False: Boolean
        """
        self.debug("MySQL Data Deletion")
        return self.master_operation(query=query)

    def master_operation(self, query: str):
        """
        Mysql Master executes SQL statements that do not return query data
        :param query: SQL query statements: String
        :return: True or False: Boolean
        """
        self.debug("MySQL Master Operations")
        return self.__operaion(query, "master")

    def slave_operation(self, query: str):
        """
        SQL statement executed by Mysql Slave does not return query data
        :param query: SQL query statements: String
        :return: True or False: Boolean
        """
        self.debug("MySQL Slave Operations")
        return self.__operaion(query, "slave")

    def __operaion(self, query: str, dbrouter: str):
        """
        Private methods execute SQL statements that do not return query data.
        :param query: SQL query statements: String
        :param dbrouter: Database routing distinguishes between Master and Slave: String
        :return: True or False: Boolean
        """
        try:
            if dbrouter == "master":
                conn = self.__connect_master_tool
            elif dbrouter == "slave":
                conn = self.__connect_slave_tool
            else:
                raise ParamsError("Method parameter error")
        except Exception as error:
            self.exception(error)
            sys.exit(1)
        cur = conn.cursor()
        try:
            cur.execute(query=query)
            conn.commit()
            self.debug("MySQL Transaction Executed Successfully：{}".format(query))
            result = True
        except Exception as error:
            conn.rollback()
            self.error("MySQL Transaction Execution Failure：{}".format(query))
            self.exception(error)
            result = False
        finally:
            cur.close()
            conn.close()
        return result
