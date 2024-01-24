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

from typing import Union, Any
import random
import pymysql

from modules.journals import Journal


class MySQLStandaloneTools:
    """MySQL Single Node Database"""

    def __init__(
        self,
        host: str,
        port: int,
        user: str,
        password: str,
        database: str,
        charset: str = "utf8mb4",
        connect_timeout: int = 10,
    ):
        """
        Initialize MySQL database connection.
            初始化MySQL数据库连接。
        @param host: Database host address. | 数据库主机地址
        @type host: str
        @param port: Database port. | 数据库端口
        @type port: int
        @param user: Database username. | 数据库用户名
        @type user: str
        @param password: Database password. | 数据库密码
        @type password: str
        @param database: Database name to connect to. | 要连接的数据库名称
        @type database: str
        @param charset: Database charset, default is 'utf8mb4'. | 数据库字符集，默认为'utf8mb4'
        @type charset: str
        @param connect_timeout: Connection timeout in seconds, default is 10. | 连接超时时间，默认为10秒
        @type connect_timeout: int
        """
        self.__host = host
        self.__port = port
        self.__user = user
        self.__password = password
        self.__database = database
        self.__charset = charset
        self.__connect_timeout = connect_timeout
        self.__init_connect()

    def __connect_process(self) -> pymysql.connections.Connection:
        """
        Handle database connection.
            处理数据库连接。
        @return: Returns the database connection object. | 返回数据库连接对象
        @rtype: pymysql.connections.Connection
        """
        try:
            connect = pymysql.connect(
                host=self.__host,
                port=self.__port,
                user=self.__user,
                password=self.__password,
                database=self.__database,
                charset=self.__charset,
                connect_timeout=self.__connect_timeout,
            )
            Journal.success("MySQL Connect: OK")
        except Exception as error:
            Journal.error(error)
            return
        return connect

    def __connect_cursor(self):
        """
        Create and return a database cursor.
            创建并返回数据库游标。
        @return: Returns the database cursor. | 返回数据库游标
        @rtype: pymysql.cursors.Cursor
        """
        try:
            results = self.__connect.cursor()
            Journal.success("MySQL Cursor: OK")
        except Exception as error:
            Journal.error(error)
            return
        return results

    def __init_connect(self) -> None:
        """
        Initialize and establish database connection and cursor.
            初始化并建立数据库连接和游标。
        """
        self.__connect = self.__connect_process()
        self.__cursor = self.__connect_cursor()

    def __close_connect(self) -> None:
        """
        Close the database connection.
            关闭数据库连接。
        """
        if self.__connect:
            self.__connect.close()
            self.__connect = None
            Journal.debug("MySQL has been disconnected.")

    def __close_cursor(self) -> None:
        """
        Close the database cursor.
            关闭数据库游标。
        """
        if self.__cursor:
            self.__cursor.close()
            self.__cursor = None
            Journal.debug("MySQL has disconnected the cursor.")

    def __reconnect(self) -> None:
        """
        Reconnect to the database.
            重连数据库。
        """
        if not self.__connect or not self.__cursor:
            Journal.debug("Wait for MySQL to reconnect.")
            if self.__connect and self.__cursor:
                self.__close_cursor()
                self.__cursor = self.__connect.cursor()
                Journal.debug("MySQL cursor has been reset.")
            elif self.__connect and not self.__cursor:
                self.__cursor = self.__connect.cursor()
                Journal.debug("MySQL cursor is connected.")
            elif not self.__connect and not self.__cursor:
                self.__connect = self.__connect_process()
                self.__cursor = self.__connect_cursor()
                Journal.warning("MySQL has been reconnected.")

    def __close(self) -> None:
        """
        Completely close the database connection and cursor.
            完全关闭数据库连接和游标。
        """
        if self.__connect and self.__cursor:
            self.__close_cursor()
            self.__close_connect()
        elif self.__connect and not self.__cursor:
            self.__close_connect()
        Journal.warning("MySQL has been disconnected the all.")

    def __trace_sql_statement(self, query, args) -> str:
        """
        Generate and return a debug SQL statement.
            生成并返回调试SQL语句。
        @param query: SQL query statement. | SQL查询语句
        @type query: str
        @param args: SQL query parameters. | SQL查询参数
        @type args: Union[tuple, list, dict, None]
        @return: Debug information. | 调试信息
        @rtype: str
        """
        return f"SQL -> {query} | Parameters -> {args}"

    def __operation(
        self,
        query: Union[str, tuple, list, set],
        args: Union[tuple, list, dict, None] = None,
    ) -> Union[tuple[tuple[Any], ...], None]:
        """
        Execute SQL operations.
            执行SQL操作。
        @param query: SQL statement(s). SQL语句
        @type query: Union[str, tuple, list, set]
        @param args: SQL parameters. | SQL参数
        @type args: Union[tuple, list, dict, None]
        @return: Operation result. | 操作结果
        @rtype: Depends on the SQL operation
        """
        try:
            self.__reconnect()
            if isinstance(query, str):
                Journal.trace(self.__trace_sql_statement(query, args))
                self.__cursor.execute(query=query, args=args)
                results = self.__cursor.fetchall()
            elif isinstance(query, (tuple, list, set)):
                results_list = []
                for query_str, query_args in zip(query, args):
                    Journal.trace(self.__trace_sql_statement(query_str, query_args))
                    self.__cursor.execute(query=query_str, args=query_args)
                    results_list.append(self.__cursor.fetchall())
            else:
                raise TypeError("Wrong SQL statement type.")
            self.__connect.commit()
        except Exception as error:
            Journal.debug("Failed to execute the rollback")
            self.__connect.rollback()
            Journal.error(error)
            return
        finally:
            self.__close_cursor()
        return results if "results" in locals() else tuple(results_list)

    def execute(self, sql, args=None) -> Union[tuple[tuple[Any], ...], None]:
        """
        Execute single or multiple SQL statements.
            执行单个或多个SQL语句。
        @param sql: SQL statement or a set of statements. | SQL语句或语句集
        @type sql: Union[str, tuple, list, set]
        @param args: Parameters for the SQL statement(s). | SQL语句的参数
        @type args: Union[tuple, list, dict, None]
        @return: Execution result. | 执行结果
        @rtype: Depends on the SQL operation
        """
        if (
            not isinstance(sql, str)
            and isinstance(sql, (list, tuple, set))
            and not args
        ):
            args = tuple([None for _ in range(len(sql))])
        return self.__operation(query=sql, args=args)

    def close(self):
        """
        Close the database connection and cursor.
            关闭数据库连接和游标。
        """
        self.__close()
