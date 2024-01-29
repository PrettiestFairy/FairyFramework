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
from controller.datasource import DataSource
from tools.datasource import PostgreSQLStandaloneSSLTools


class TestClass:
    """Test Class"""

    @TimeDecorators
    @MethodDecorators(annotation="测试方法")
    def test(self):
        # sql_query = (
        #     "select * from tb_douban_movies.tb_movies_used_info where id <= %(id)s;",
        #     "select count(id) from tb_douban_movies.tb_movies_used_info;",
        # "insert into public_db_test.tb_test(name) values (%(name1)s), (%(name2)s);",
        # "update public_db_test.tb_test set status = false, update_time = now() where id <= %(id)s;",
        # "select * from public_db_test.tb_test;",
        # )
        # # sql_args = ({"id": 1}, None, {"name1": "于萌萌", "name2": "邵磊"}, {"id": "10"}, None)
        # sql_args = ({"id": 2}, None)
        # results = DataSource.controller.execute(sql_query, sql_args)
        # Journal.debug(results)
        # DataSource.controller.close()
        # if results:
        #     Journal.debug("查询成功")
        # sql = "select * from tb_douban_movies.tb_movies_used_info where directors = %s;"
        # r1 = DataSource.controller.execute(sql, args="张吃鱼")
        # if r1:
        #     # print(r1)
        #     Journal.debug("查询成功")
        # sql = (
        #     "select version();",
        #     "select version();",
        #     "select * from internal_app_hnlt_dev.host where id = %(id)s;",
        # )
        # sql_vars = (None, None, {"id": 35})
        # a = DataSource.controller.execute(sql, parameters=sql_vars)
        datasource = PostgreSQLStandaloneSSLTools(
            ssh_host="10.65.66.167",
            ssh_port=22,
            ssh_username="root",
            ssh_password="xajf!@#123",
            remote_host="10.65.66.167",
            remote_port=5432,
            host="localhost",
            port=5432,
            user="nsc",
            password="nsc",
            database="nsc",
        )
        print(datasource.execute("select version();"))
        # DataSource.controller.close()


def main(*args, **kwargs):
    test = TestClass()
    test.test()


def test():
    import time

    time.sleep(5)


if __name__ == "__main__":
    main()
    # test()
