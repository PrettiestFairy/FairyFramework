# coding: utf8
""" 
@File: mysql.py
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

_controller = MySQLStandaloneTools(
    host=MySQLStandaloneConfig.host,
    port=MySQLStandaloneConfig.port,
    user=MySQLStandaloneConfig.user,
    password=MySQLStandaloneConfig.password,
    database=MySQLStandaloneConfig.database,
    charset=MySQLStandaloneConfig.charset,
)


class MySQLStandalone:
    """MySQl Standalone Controller"""

    global _controller
    controller = _controller
