# coding: utf8
""" 
@File: source.py
@Editor: PyCharm
@Author: Austin (From Chengdu.China) https://fairy.host
@HomePage: https://github.com/AustinFairyland
@OperatingSystem: Windows 11 Professional Workstation 23H2 Canary Channel
@CreatedTime: 2024-01-24
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

from tools.datasource import MySQLStandaloneTools
from modules.configuration import MySQLStandaloneConfig
from tools.datasource import PostgreSQLStandaloneTools
from modules.configuration import PostgreSQLStandaloneConfig


_mysql_controller = MySQLStandaloneTools(
    host=MySQLStandaloneConfig.host,
    port=MySQLStandaloneConfig.port,
    user=MySQLStandaloneConfig.user,
    password=MySQLStandaloneConfig.password,
    database=MySQLStandaloneConfig.database,
    charset=MySQLStandaloneConfig.charset,
)

_postgresql_controller = PostgreSQLStandaloneTools(
    host=PostgreSQLStandaloneConfig.host,
    port=PostgreSQLStandaloneConfig.port,
    user=PostgreSQLStandaloneConfig.user,
    password=PostgreSQLStandaloneConfig.password,
    database=PostgreSQLStandaloneConfig.database,
)


class MySQLStandalone:
    """MySQlStandaloneController"""

    controller = _mysql_controller


class PostgreSQLStandalone:
    """PostgreSQLStandalone"""

    controller = _postgresql_controller
