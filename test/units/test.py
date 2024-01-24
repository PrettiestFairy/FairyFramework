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
from controller.datasource import MySQLStandalone


class TestClass:
    def test(self):
        sql_query = (
            "select id, name from public_db_test.tb_test where id = %(id)s;",
            "select count(id) from public_db_test.tb_test;",
            # "insert into public_db_test.tb_test(name) values (%(name1)s), (%(name2)s);",
            # "update public_db_test.tb_test set status = false, update_time = now() where id <= %(id)s;",
            "select * from public_db_test.tb_test;",
        )
        # sql_args = ({"id": 1}, None, {"name1": "于萌萌", "name2": "邵磊"}, {"id": "10"}, None)
        sql_args = ({"id": 1}, None, None)
        results = MySQLStandalone.controller.execute(sql_query, sql_args)
        Journal.debug(results)
        user_1_info, user_total, user_info = results
        for user_1_id, user_1_name in user_1_info:
            Journal.debug(f"用户ID: {user_1_id}, 用户名: {user_1_name}")
        ((user_total,),) = user_total
        Journal.debug(f"用户总数: {user_total}")
        for _id, _name, _create_time, _update_time, _status in user_info:
            if _status:
                _status = True
            else:
                _status = False
            _id: int
            _name: str
            _create_time: datetime
            _update_time: datetime
            _status: int
            Journal.debug(
                f"用户ID: {_id}, 用户名: {_name}, 创建时间: {_create_time.timestamp().__int__()}, 修改时间: {_update_time.strftime('%Y-%m-%d %H:%M:%S')}, 用户状态: {_status}"
            )
        a = MySQLStandalone.controller.execute("select aa from public_db_test.tb_test;")
        print(a)
        MySQLStandalone.controller.close()


def main(*args, **kwargs):
    test = TestClass()
    test.test()


def test():
    from pyfiglet import Figlet
    f = Figlet("slant", width=120)
    print(f.renderText("Austin Framework"))


if __name__ == "__main__":
    main()
    # test()
