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

import pymysql

# from modules.journals import JournalsModuleClass
from conf import ConfigClass


class MySQLStandaloneToolsClass:
    """ MySQL 单节点数据库 """

    def __init__(self):
        JournalsModuleClass.debug('初始化类：{}'.format(self.__class__.__name__))
        try:
            self.__mysql_config: dict = ConfigClass.config.get('datasource').get('mysql').get('standalone')
        except Exception as error:
            JournalsModuleClass.exception(error)
            sys.exit(1)

        # self.__connect = self.__connect_tool
        # self.__cursor = self.__cursor_tool()

    @property
    def __connect_tool(self):
        """
        MySQL 连接
        :return: MySQL Connect Object MySQL 连接对象
        """
        try:
            if self.__mysql_config is None:
                raise Exception('MySQL 数据源配置错误')
            __host = self.__mysql_config.get('host')
            __port = self.__mysql_config.get('port')
            __user = self.__mysql_config.get('user')
            __password = self.__mysql_config.get('password')
            __database = self.__mysql_config.get('database')
            __charset = self.__mysql_config.get('charset')
            if __charset is None:
                __charset = 'utf8mb4'
            if __host is None or __port is None or __user is None or __password is None or __database is None:
                raise Exception('MySQL 数据源配置错误')
            JournalsModuleClass.debug('MySQL 数据源：MySQL Standalone')
            JournalsModuleClass.debug('MySQL IP：{}'.format(__host))
            JournalsModuleClass.debug('MySQL 端口：{}'.format(__port))
            JournalsModuleClass.debug('MySQL 用户名：{}'.format(__user))
            JournalsModuleClass.debug('MySQL 数据库：{}'.format(__database))
            JournalsModuleClass.debug('MySQL 字符集：{}'.format(__charset))
            connect = pymysql.connect(
                host=__host,
                port=__port,
                user=__user,
                password=__password,
                database=__database,
                charset=__charset
            )
            JournalsModuleClass.debug('MySQL 连接成功')
            return connect
        except Exception as error:
            JournalsModuleClass.exception(error)
            sys.exit(1)

    # def __cursor_tool(self):
    #     return self.__connect.cursor()

    def query(self, query: str):
        """
        MySQL 数据查询
        :param query: String SQL 查询语句
        :return: Iteratable Object 查询结果
        """
        JournalsModuleClass.debug('MySQL 数据查询')
        conn = self.__connect_tool
        cur = conn.cursor()
        try:
            cur.execute(query=query)
            result = cur.fetchall()
            conn.commit()
        except Exception as error:
            result = None
            conn.rollback()
            JournalsModuleClass.debug('查询事务执行成功：{}'.format(query))
            JournalsModuleClass.exception(error)
        finally:
            cur.close()
            conn.cursor()
        return result

    def __operation(self, query: str):
        """
        私有方法 执行的 SQL 语句不返回查询数据
        :param query: String SQL 查询语句
        :return: Boolean
        """
        conn = self.__connect_tool
        cur = conn.cursor()
        try:
            cur.execute(query=query)
            conn.commit()
            JournalsModuleClass.debug('MySQL 事务执行成功：{}'.format(query))
            result = True
        except Exception as error:
            conn.rollback()
            JournalsModuleClass.error('MySQL 事务执行失败：{}'.format(query))
            JournalsModuleClass.exception(error)
            result = False
        finally:
            cur.close()
            conn.close()
        return result

    def operation(self, query: str):
        """
        执行的 SQL 语句不返回查询数据
        :param query: String SQL 查询语句
        :return: Boolean
        """
        JournalsModuleClass.debug('MySQL 操作')
        return self.__operation(query=query)

    def insert(self, query: str):
        """
        插入 SQL 数据
        :param query: String SQL 插入语句
        :return: Boolean
        """
        JournalsModuleClass.debug('MySQL 数据插入')
        return self.__operation(query=query)

    def update(self, query: str):
        """
        更新 SQL 数据
        :param query: String SQL 更新语句
        :return: Boolean
        """
        JournalsModuleClass.debug('MySQL 数据更新')
        return self.__operation(query=query)

    def delete(self, query: str):
        """
        删除 SQL 数据
        :param query: String SQL 删除语句
        :return: Boolean
        """
        JournalsModuleClass.debug('MySQL 数据删除')
        return self.__operation(query=query)


class MySQLMasterSlaveDBRouterToolsClass:
    """ MySQL 数据库读写分离 """

    def __init__(self):
        JournalsModuleClass.debug('初始化类：{}'.format(self.__class__.__name__))
        try:
            self.__mysql_config: dict = ConfigClass.config.get('datasource').get('mysql').get('dbrouter')
        except Exception as error:
            JournalsModuleClass.exception(error)
            sys.exit(1)

    def __mysql_master_config(self) -> dict:
        """
        获取 Master 配置信息
        :return: Dict Master 配置信息
        """
        try:
            mysql_config_master: list = self.__mysql_config.get('master')
            return random.choice(mysql_config_master)
        except Exception as error:
            JournalsModuleClass.exception(error)
            sys.exit(1)

    def __mysql_slave_config(self) -> dict:
        """
        获取 Slave 配置信息
        :return: Dict Slave 配置信息
        """
        try:
            mysql_config_slave: list = self.__mysql_config.get('slave')
            return random.choice(mysql_config_slave)
        except Exception as error:
            JournalsModuleClass.exception(error)
            sys.exit(1)

    @property
    def __connect_master_tool(self):
        """
        MySQL Master 连接
        :return: Mysql Connect Object Mysql 连接对象
        """
        try:
            __master_config = self.__mysql_master_config()
            __master_host = __master_config.get('host')
            __master_port = __master_config.get('port')
            __master_user = __master_config.get('user')
            __master_password = __master_config.get('password')
            __master_database = __master_config.get('database')
            __master_charset = __master_config.get('charset')
            if __master_charset is None:
                __master_charset = 'utf8mb4'
            if __master_host is None or __master_port is None or __master_user is None or __master_password is None or __master_database is None:
                raise Exception('MySQL Master 数据源配置错误')
            JournalsModuleClass.debug('MySQL 数据源：MySQL Master DBRouter')
            JournalsModuleClass.debug('MySQL IP：{}'.format(__master_host))
            JournalsModuleClass.debug('MySQL 端口：{}'.format(__master_port))
            JournalsModuleClass.debug('MySQL 用户名：{}'.format(__master_user))
            JournalsModuleClass.debug('MySQL 数据库：{}'.format(__master_database))
            JournalsModuleClass.debug('MySQL 字符集：{}'.format(__master_charset))
            connect = pymysql.connect(
                host=__master_host,
                port=__master_port,
                user=__master_user,
                password=__master_password,
                database=__master_database,
                charset=__master_charset
            )
            return connect
        except Exception as error:
            JournalsModuleClass.exception(error)
            sys.exit(1)

    @property
    def __connect_slave_tool(self):
        """
        MySQL Slave 连接
        :return: Mysql Connect Object Mysql 连接对象
        """
        try:
            __slave_config = self.__mysql_slave_config()
            __slave_host = __slave_config.get('host')
            __slave_port = __slave_config.get('port')
            __slave_user = __slave_config.get('user')
            __slave_password = __slave_config.get('password')
            __slave_database = __slave_config.get('database')
            __slave_charset = __slave_config.get('charset')
            if __slave_charset is None:
                __slave_charset = 'utf8mb4'
            if __slave_host is None or __slave_port is None or __slave_user is None or __slave_password is None or __slave_database is None:
                raise Exception('MySQL Slave 数据源配置错误')
            JournalsModuleClass.debug('MySQL 数据源：MySQL Slave DBRouter')
            JournalsModuleClass.debug('MySQL IP：{}'.format(__slave_host))
            JournalsModuleClass.debug('MySQL 端口：{}'.format(__slave_port))
            JournalsModuleClass.debug('MySQL 用户名：{}'.format(__slave_user))
            JournalsModuleClass.debug('MySQL 数据库：{}'.format(__slave_database))
            JournalsModuleClass.debug('MySQL 字符集：{}'.format(__slave_charset))
            connect = pymysql.connect(
                host=__slave_host,
                port=__slave_port,
                user=__slave_user,
                password=__slave_password,
                database=__slave_database,
                charset=__slave_charset
            )
            return connect
        except Exception as error:
            JournalsModuleClass.exception(error)
            sys.exit(1)

    def query(self, query: str):
        """
        MySQL 数据查询
        :param query: String SQL 查询语句
        :return: Iteratable Object 查询结果
        """
        JournalsModuleClass.debug('MySQL 数据查询')
        conn = self.__connect_slave_tool
        cur = conn.cursor()
        try:
            cur.execute(query=query)
            result = cur.fetchall()
            conn.commit()
        except Exception as error:
            result = None
            conn.rollback()
            JournalsModuleClass.exception(error)
        finally:
            cur.close()
            conn.close()
        return result

    def inster(self, query: str):
        """
        插入 SQL 数据
        :param query: String SQL 插入语句
        :return: Boolean
        """
        JournalsModuleClass.debug('MySQL 数据插入')
        return self.master_operation(query=query)

    def update(self, query: str):
        """
        更新 SQL 数据
        :param query: String SQL 更新语句
        :return: Boolean
        """
        JournalsModuleClass.debug('MySQL 数据更新')
        return self.master_operation(query=query)

    def delete(self, query: str):
        """
        删除 SQL 数据
        :param query: String SQL 删除语句
        :return: Boolean
        """
        JournalsModuleClass.debug('MySQL 数据删除')
        return self.master_operation(query=query)

    def master_operation(self, query: str):
        """
        Mysql Master 执行的 SQL 语句不返回查询数据
        :param query: String SQL 查询语句
        :return: Boolean
        """
        JournalsModuleClass.debug('MySQL Master 操作')
        return self.__operaion(query, 'master')

    def slave_operation(self, query: str):
        """
        Mysql Slave 执行的 SQL 语句不返回查询数据
        :param query: String SQL 查询语句
        :return: Boolean
        """
        JournalsModuleClass.debug('MySQL Slave 操作')
        return self.__operaion(query, 'slave')

    def __operaion(self, query: str, dbrouter: str):
        """
        私有方法 执行的 SQL 语句不返回查询数据
        :param query: String SQL 查询语句
        :param dbrouter: String 数据库路由 分辨是用 Master 还是 Slave
        :return: Boolean
        """
        try:
            if dbrouter == 'master':
                conn = self.__connect_master_tool
            elif dbrouter == 'slave':
                conn = self.__connect_slave_tool
            else:
                raise Exception('方法参数错误')
        except Exception as error:
            JournalsModuleClass.exception(error)
            sys.exit(1)
        try:
            cur = conn.cursor()
            cur.execute(query=query)
            conn.commit()
            JournalsModuleClass.debug('MySQL 事务执行成功：{}'.format(query))
            result = True
        except Exception as error:
            conn.rollback()
            JournalsModuleClass.error('MySQL 事务执行失败：{}'.format(query))
            JournalsModuleClass.exception(error)
            result = False
        finally:
            cur.close()
            conn.close()
        return result
