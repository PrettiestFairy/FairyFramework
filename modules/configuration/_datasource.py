# coding: utf8
""" 
@File: _datasource.py
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

from modules.journals import Journal
from ._configurations import config


class DataSourceConfig:
    """Mysql Standalone Config"""

    load_dotenv()
    __DATASOURCE = os.getenv("DATASOURCE", "MySQL")

    if __DATASOURCE == "MySQL":
        Journal.info("MySQL Data Source: MySQL Standlone.")
        __mysql_config: dict = (
            config.get("datasource", {}).get("mysql", {}).get("standalone", {})
        )
        if __mysql_config:
            Journal.success("The MySQL configuration was read successfully. Procedure")
        else:
            Journal.error("Failed to read the MySQL configuration.")
        host = __mysql_config.get("host", "127.0.0.1")
        port = __mysql_config.get("port", 3306)
        user = __mysql_config.get("user", "root")
        password = __mysql_config.get("password", "root")
        database = __mysql_config.get("database", "public_default")
        charset = __mysql_config.get("charset", "utf8mb4")
        connect_timeout = __mysql_config.get("timeout", 10)
        Journal.info(f"MySQL Standalone host: {host}")
        Journal.info(f"MySQL Standalone port: {port}")
        Journal.info(f"MySQL Standalone user: {user}")
        Journal.trace(f"MySQL Standalone password: {password}")
        Journal.info(f"MySQL Standalone database: {database}")
        Journal.info(f"MySQL Standalone charset: {charset}")
    elif __DATASOURCE == "PostgreSQL":
        Journal.info("PostgreSQL Data Source: PostgreSQL Standlone.")
        __postgresql_config: dict = (
            config.get("datasource", {}).get("postgresql", {}).get("standalone", {})
        )
        if __postgresql_config:
            Journal.success(
                "The PostgreSQL configuration was read successfully. Procedure"
            )
        else:
            Journal.error("Failed to read the PostgreSQL configuration.")
        host = __postgresql_config.get("host", "127.0.0.1")
        port = __postgresql_config.get("port", 5432)
        user = __postgresql_config.get("user", "postgres")
        password = __postgresql_config.get("password", None)
        database = __postgresql_config.get("database", "postgres")
        Journal.info(f"PostgreSQL Standalone host: {host}")
        Journal.info(f"PostgreSQL Standalone port: {port}")
        Journal.info(f"PostgreSQL Standalone user: {user}")
        Journal.trace(f"PostgreSQL Standalone password: {password}")
        Journal.info(f"PostgreSQL Standalone database: {database}")
