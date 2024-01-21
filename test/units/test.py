# coding: utf8
""" 
@File: test.py
@Editor: PyCharm
@Author: Austin (From Chengdu.China) https://fairy.host
@HomePage: https://github.com/AustinFairyland
@OperatingSystem: Windows 11 Professional Workstation 23H2 Canary Channel
@CreatedTime: 2023-10-11
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

from modules.journals import Journal
from tools.database import MySQLStandaloneToolsClass
from modules.inheritance import Base
from modules.configuration import Config


class TestClass:

    def test(self):
        config = Config.config()
        print(config.get("datasource"))
        return ""


def main(*args, **kwargs):
    test = TestClass()
    Journal.debug(test.test())


if __name__ == "__main__":
    main()
