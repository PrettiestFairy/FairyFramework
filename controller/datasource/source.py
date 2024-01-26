# coding: utf8
""" 
@File: _source.py
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

from dotenv import load_dotenv

from modules.configuration import DataSourceConfig
from tools.datasource import MySQLStandaloneTools
from tools.datasource import PostgreSQLStandaloneTools

load_dotenv()
__DATASOURCE = os.getenv("DATASOURCE", "MySQL")

if __DATASOURCE == "MySQL":
    _controller = MySQLStandaloneTools(
        host=DataSourceConfig.host,
        port=DataSourceConfig.port,
        user=DataSourceConfig.user,
        password=DataSourceConfig.password,
        database=DataSourceConfig.database,
        charset=DataSourceConfig.charset,
    )
elif __DATASOURCE == "PostgreSQL":
    _controller = PostgreSQLStandaloneTools(
        host=DataSourceConfig.host,
        port=DataSourceConfig.port,
        user=DataSourceConfig.user,
        password=DataSourceConfig.password,
        database=DataSourceConfig.database,
    )


class DataSource:
    """DataSource"""

    controller = _controller
