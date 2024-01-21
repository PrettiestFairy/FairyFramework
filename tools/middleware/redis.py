# coding: utf8
""" 
@File: redis.py
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

from redis import ConnectionPool
from redis import Redis
from rediscluster import RedisCluster
from rediscluster.connection import ClusterConnectionPool

from modules.inheritance import Base


class RedisStandaloneToolsClass(Base):
    """Redis Single Node Tool Class"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.debug("Initialization class：{}".format(self.__class__.__name__))
        try:
            self.__redis_config: dict = (
                self.config.get("middleware").get("redis").get("standalone")
            )
        except Exception as error:
            self.exception(error)
            sys.exit(1)

    @property
    def __redis_connect(self):
        """
        Redis Connections
        :return: Connect Object: Redis Connect Object
        """
        try:
            __host = self.__redis_config.get("host")
            __port = self.__redis_config.get("port")
            __password = self.__redis_config.get("password")
            __db = self.__redis_config.get("db")
            pool = ConnectionPool(
                host=__host,
                port=__port,
                password=__password,
                db=__db,
                decode_responses=True,
                max_connections=10,
            )
            conn = Redis(connection_pool=pool)
            self.debug("Redis Server Connection Successful")
            return conn
        except Exception as error:
            self.exception(error)
            sys.exit(1)

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


class RedisClusterToolsClass(Base):
    """Redis 集群工具类"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.debug("Initialization class：{}".format(self.__class__.__name__))
        try:
            self.__redis_config: list = (
                self.config.get("middleware").get("redis").get("cluster")
            )
        except Exception as error:
            self.exception(error)

    @property
    def __redis_cluster_connect(self):
        try:
            redis_cluster_confg = (
                self.config.get("middleware").get("redis").get("cluster")
            )
            startup_nodes = []
            __password_map = {}
            for standalone_confg in redis_cluster_confg:
                standalone_confg: dict
                __host = standalone_confg.get("host")
                __port = standalone_confg.get("port")
                __password = standalone_confg.get("password")
                startup_nodes.append({"host": __host, "port": __port})
                __password_map["{}:{}".format(__host, __port)] = __password
            self.debug("Redis Connection Pool Data Sources：{}".format(startup_nodes))
            pool = ClusterConnectionPool(
                startup_nodes=startup_nodes,
                password_map=__password_map,
                max_connections=10,
                decode_responses=True,
            )
            conn = RedisCluster(connection_pool=pool)
            self.debug("Redis Cluster Connection Successful")
            return conn
        except Exception as error:
            self.error("Redis Cluster Connection Failure")
            self.exception(error)

    def redis_get(self, k):
        conn = self.__redis_cluster_connect
        try:
            value = conn.get(k)
            self.debug(
                "Redis Fetches Data Successfully：key：{}，value：{}".format(k, value)
            )
            return value
        except Exception as error:
            self.exception(error)
        finally:
            conn.connection_pool.disconnect()
