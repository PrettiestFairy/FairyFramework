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

import os
import sys
import warnings
import platform
import asyncio

sys.dont_write_bytecode = True
warnings.filterwarnings("ignore")
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from datetime import datetime
from typing import Any

from modules.journals import Journal
from modules.decorator import MethodDecorators
from modules.decorator import TimeDecorators
from controller.datasource import MySQLStandalone


class TestClass:
    """Test Class"""

    @TimeDecorators
    @MethodDecorators(annotation="测试方法")
    def test(self):
        sql_query = (
            "select * from tb_douban_movies.tb_movies_used_info where id <= %(id)s;",
            "select count(id) from tb_douban_movies.tb_movies_used_info;",
            # "insert into public_db_test.tb_test(name) values (%(name1)s), (%(name2)s);",
            # "update public_db_test.tb_test set status = false, update_time = now() where id <= %(id)s;",
            # "select * from public_db_test.tb_test;",
        )
        # sql_args = ({"id": 1}, None, {"name1": "于萌萌", "name2": "邵磊"}, {"id": "10"}, None)
        sql_args = ({"id": 2}, None, None)
        results = MySQLStandalone.controller.execute(sql_query, sql_args)
        if results:
            Journal.debug("查询成功")
        sql = "select * from tb_douban_movies.tb_movies_used_info where directors = %s;"
        r1 = MySQLStandalone.controller.execute(sql, args="张吃鱼")
        if r1:
            print(r1)
            Journal.debug("查询成功")
        MySQLStandalone.controller.close()


@TimeDecorators
@MethodDecorators("主方法")
def main(*args, **kwargs):
    test = TestClass()
    test.test()


@TimeDecorators
@MethodDecorators("测试方法")
def test():
    import time

    time.sleep(5)


if __name__ == "__main__":
    main()
    # test()
