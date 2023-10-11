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

import os
import sys
import warnings
import platform
import asyncio

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')
if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import time
import random

from redis import ConnectionPool
from redis import Redis
from rediscluster import RedisCluster
from rediscluster import ClusterBlockingConnectionPool
from rediscluster import ClusterConnectionPool

from modules.journals import JournalsModuleClass
from conf import ConfigClass


class RedisStandaloneToolsClass:
    """ Redis 单节点工具类"""

    def __init__(self):
        JournalsModuleClass.debug('初始化类：{}'.format(self.__class__.__name__))
        try:
            self.__redis_config: dict = ConfigClass.config.get('middleware').get('redis').get('standalone')
        except Exception as error:
            JournalsModuleClass.exception(error)
            sys.exit(1)
        self.__connect = self.__redis_connect

    @property
    def __redis_connect(self):
        """
        Redis 连接
        :return: Redis Connect Object Redis 连接对象
        """
        try:
            __host = self.__redis_config.get('host')
            __port = self.__redis_config.get('port')
            __password = self.__redis_config.get('password')
            __db = self.__redis_config.get('db')
            JournalsModuleClass.debug('Redis 数据源：Redis Standalone')
            JournalsModuleClass.debug('Redis IP：{}'.format(__host))
            JournalsModuleClass.debug('Redis 端口：{}'.format(__port))
            JournalsModuleClass.debug('Redis 数据库：{}'.format(__db))
            pool = ConnectionPool(
                host=__host,
                port=__port,
                password=__password,
                db=__db,
                decode_responses=True,
                max_connections=10
            )
            conn = Redis(connection_pool=pool)
            JournalsModuleClass.debug('Redis 连接成功')
            return conn
        except Exception as error:
            JournalsModuleClass.exception(error)
            sys.exit(1)

    def redis_set(self, k, v):
        """
        Redis 写入数据
        :param k: 键
        :param v: 值
        :return: Boolean
        """
        try:
            self.__connect.set(k, v)
            JournalsModuleClass.debug('Redis 写入数据： key：{}， value：{}'.format(k, v))
            return True
        except Exception as error:
            JournalsModuleClass.exception(error)

    def redis_get(self, k):
        """
        Redis 根据键获取值
        :param k: 
        :return: 值
        """
        try:
            v = self.__connect.get(k)
            JournalsModuleClass.debug('Redis 读取数据： key：{}， value：{}'.format(k, v))
            return v
        except Exception as error:
            JournalsModuleClass.exception(error)
