# coding: utf8
""" 
@File: datasource.py
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

import time
import random

from modules.journals import Journal
from .configurations import config


class MySQLStandaloneConfig:
    """Mysql Standalone Config"""

    Journal.info("MySQL Data Source: MySQL Standlone.")
    __mysql_config: dict = (
        config.get("datasource", {}).get("mysql", {}).get("standalone", None)
    )
    if __mysql_config:
        Journal.success("The MySQL configuration was read successfully. Procedure")
    else:
        Journal.error("Failed to read the MySQL configuration.")
    host = __mysql_config.get("host")
    port = __mysql_config.get("port")
    user = __mysql_config.get("user")
    password = __mysql_config.get("password")
    database = __mysql_config.get("database")
    charset = __mysql_config.get("charset")
    Journal.info(f"MySQL Standalone host: {host}")
    Journal.info(f"MySQL Standalone port: {port}")
    Journal.info(f"MySQL Standalone user: {user}")
    Journal.trace(f"MySQL Standalone password: {password}")
    Journal.info(f"MySQL Standalone database: {database}")
    Journal.info(f"MySQL Standalone charset: {charset}")


class PostgreSQLStandaloneConfig:
    """PostgreSQLStandaloneConfig"""

    Journal.info("PostgreSQL Data Source: PostgreSQL Standlone.")
    __postgresql_config: dict = (
        config.get("datasource", {}).get("postgresql", {}).get("standalone", None)
    )
    if __postgresql_config:
        Journal.success("The PostgreSQL configuration was read successfully. Procedure")
    else:
        Journal.error("Failed to read the PostgreSQL configuration.")
    __postgresql_config = {
        "host": "",
        "port": "",
        "user": "",
        "password": "",
        "database": "",
    }
    host = __postgresql_config.get("host")
    port = __postgresql_config.get("port")
    user = __postgresql_config.get("user")
    password = __postgresql_config.get("password")
    database = __postgresql_config.get("database")
    Journal.info(f"PostgreSQL Standalone host: {host}")
    Journal.info(f"PostgreSQL Standalone port: {port}")
    Journal.info(f"PostgreSQL Standalone user: {user}")
    Journal.trace(f"PostgreSQL Standalone password: {password}")
    Journal.info(f"PostgreSQL Standalone database: {database}")
