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

# from tools.public import PublicToolsBaseClass
# from modules.journals import JournalModulesClass
# from modules.decorator import TimeDecorators
# from tools.public import DateTimeClass
# from modules.inheritance import BaseClass
# from tools.database import MySQLStandaloneToolsClass
# from tools.database import MySQLMasterSlaveDBRouterToolsClass
# from modules.decorator import MethodDecorators

import gmpy2
import hashlib

# from 
from austin_module_daily_tools import DateTimeClass
from austin_module_daily_tools import PublicToolsBaseClass



# class TestClass(MySQLStandaloneToolsClass, MySQLMasterSlaveDBRouterToolsClass, BaseClass):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
# 
#     @MethodDecorators(annotation="Query Method")
#     def method(self):
#         sql = "select * from public_db_test.tb_test;"
#         a = self.query(sql)
#         print(a)
#         return True

# @MethodDecorators(annotation="123")
# def te():
#     print(1)

def main(*args, **kwargs):
    print(DateTimeClass.normdatetime())
    print(PublicToolsBaseClass.obtain_root_path())
    pass
    # journal = JournalModulesClass()
    # test = TestClass()
    # for i in TestClass.__mro__:
    #     journal.debug("{}".format(i))
    # print(test.method())
    # print(te())


if __name__ == "__main__":
    main()
