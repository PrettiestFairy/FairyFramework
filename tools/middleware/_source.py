# coding: utf8
""" 
@File: _source.py
@Editor: PyCharm
@Author: Austin (From Chengdu.China) https://fairy.host
@HomePage: https://github.com/AustinFairyland
@OperatingSystem: Windows 11 Professional Workstation 23H2 Canary Channel
@CreatedTime: 2024-01-26
"""
from __future__ import annotations

import os
import sys
import warnings
import platform
import asyncio

sys.dont_write_bytecode = True
warnings.filterwarnings("ignore")
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from dotenv import load_dotenv

from redis import ConnectionPool
from redis import Redis

from modules.journals import Journal

load_dotenv()


class RedisStandaloneTools:
    """Redis Single Node Tool Class"""

    def __init__(
        self,
        host: str = "127.0.0.1",
        port: int = 6379,
        password: str = "",
        database: int = 0,
        decode_responses: bool = True,
        max_connections: int = 10,
    ):
        self.__host = host
        self.__port = port
        self.__password = password
        self.__database = database
        self.__decode_responses = decode_responses
        self.__max_connections = max_connections

    @property
    def __redis_connect(self):
        """
        Redis Connections
        :return: Connect Object: Redis Connect Object
        """
        try:
            __pool = ConnectionPool(
                host=self.__host,
                port=self.__port,
                password=self.__password,
                db=self.__database,
                decode_responses=self.__decode_responses,
                max_connections=self.__max_connections,
            )
            conn = Redis(connection_pool=__pool)
            Journal.debug("Redis Server Connection Successful")
        except Exception as error:
            Journal.error(error)
            raise
        return conn

    def redis_set(self, k, v):
        """
        Redis Write Data
        :param k: Key: String
        :param v: Value: Any
        :return: True or False: Boolean
        """
        conn = self.__redis_connect
        try:
            conn.set(k, v)
            return True
        except Exception as error:
            self.exception(error)
        finally:
            conn.connection_pool.disconnect()

    def redis_get(self, k):
        """
        Redis Fetches Values Based on Keys
        :param k: key: String
        :return: Value: Any
        """
        conn = self.__redis_connect
        try:
            v = conn.get(k)
            self.debug("Redis Fetches Data Successfully： key：{}， value：{}".format(k, v))
            return v
        except Exception as error:
            self.exception(error)
        finally:
            conn.connection_pool.disconnect()
