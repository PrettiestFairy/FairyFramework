# coding: utf8
""" 
@File: generate.py
@Editor: PyCharm
@Author: Austin (From Chengdu.China) https://fairy.host
@HomePage: https://github.com/AustinFairyland
@OperatingSystem: Windows 11 Professional Workstation 23H2 Canary Channel
@CreatedTime: 2024-01-19
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

from pypika import MySQLQuery, Field, Database, Schema, Table


class BuildMySQL:
    def __init__(self, database):
        self.__database = Database(database)

    def __table(self, name):
        return Table(name)
    
    def __select(self, field_iterable):
        results = MySQLQuery.from_("tb_name").select(*field_iterable)
        return results

    def test(self):
        a = self.__select(("id", "name"))
        print(a.get_sql())


if __name__ == "__main__":
    build_sql = BuildMySQL("internal_db_test")
    build_sql.test()
