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

from modules.journals import JournalModules
from tools.database import MySQLStandaloneToolsClass
from modules.inheritance import Base


class TestClass(MySQLStandaloneToolsClass, Base):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # @MethodDecorators(annotation="Query Method")
    def method(self):
        sql = "select id from public_db_test.tb_test;"
        a = self.query(sql)
        print(a)
        # for _id, _name, _update_time in a:
        #     print(_id)
        #     print(_name)
        #     print(_update_time)
        for _id in (_id for row in a for _id in row):
            print(_id)
        return True

def main(*args, **kwargs):
    jouranl = JournalModules()
    test = TestClass()
    jouranl.debug(test.method())


if __name__ == "__main__":
    main()
