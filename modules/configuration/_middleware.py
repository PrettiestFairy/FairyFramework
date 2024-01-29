# coding: utf8
""" 
@File: _middleware.py
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

from modules.journals import Journal
from ._configurations import config

class BufferMiddlewareConfig:
    
    load_dotenv()
    __BUFFER_DATA = os.getenv("BUFFER_DATA")
    
    if __BUFFER_DATA == "Redis":
        Journal.info("Redis Data Source: Redis Standlone.")
        __Redis_config: dict = (
            config.get("datasource", {}).get("Redis", {}).get("standalone", {})
        )
        if __Redis_config:
            Journal.success("The Redis configuration was read successfully. Procedure")
        else:
            Journal.error("Failed to read the Redis configuration.")
        host = __Redis_config.get("host", "127.0.0.1")
        port = __Redis_config.get("port", 3306)
        user = __Redis_config.get("user", "root")
        password = __Redis_config.get("password", "root")
        database = __Redis_config.get("database", "public_default")
        charset = __Redis_config.get("charset", "utf8mb4")
        Journal.info(f"Redis Standalone host: {host}")
        Journal.info(f"Redis Standalone port: {port}")
        Journal.info(f"Redis Standalone user: {user}")
        Journal.trace(f"Redis Standalone password: {password}")
        Journal.info(f"Redis Standalone database: {database}")
