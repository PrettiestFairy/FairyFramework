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
warnings.filterwarnings('ignore')
if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from typing import Any
import time

from tools.publics import PublicToolsBaseClass
from modules.journals import JournalModulesClass
from conf import ConfigClass


class TestClass:

    def __init__(self):
        pass

    def test_task_01(self) -> Any:
        public_tools = PublicToolsBaseClass()
        journal_modules = JournalModulesClass()
        global_config = ConfigClass()
        config = global_config.config()
        journal_modules.debug('运行配置：{}'.format(config))
        redis_cluster_confg = config.get('middleware').get('redis').get('cluster')
        cluster_confg_list: list = []
        __password_map: dict = {}
        for standalone_confg in redis_cluster_confg:
            standalone_confg: dict
            __host = standalone_confg.get('host')
            __port = standalone_confg.get('port')
            __password = standalone_confg.get('password')
            cluster_confg_list.append({'host': __host, 'port': __port})
            __password_map['{}:{}'.format(__host, __port)] = __password
        journal_modules.info(cluster_confg_list)
        journal_modules.info(__password_map)
        # print(config.get('datasource')['mysql']['dbrouter'])
        # mysql = MySQLStandaloneToolsClass()
        # mysql_db_router = MySQLMasterSlaveDBRouterToolsClass()
        # mysql.update("""insert into test(name, score) values ('c', 100), ('c', 50);""")
        # d = mysql.query('select * from test;')
        # for i in d:
        #     print(i)
        # mysql_db_router.inster(query="""insert into test(name, score) values ('c', 100), ('c', 50);""")
        # mysql_db_router.slave_operation(query="""show tables;""")
        # d = mysql_db_router.query('select * from test;')
        # for i in d:
        #     print(i)
        # _redis = RedisStandaloneToolsClass()
        # _redis.redis_set('code', 1234)
        # d = _redis.redis_get('code')
        return 'test_task_01 测试完成'

    def test_task_02(self):
        pass


if __name__ == '__main__':
    start_run_time = time.time()
    journal_modules = JournalModulesClass()

    TestClass.test_task_01(TestClass)
    # t_cls = TestClass()
    # journal_modules.debug(t_cls.test_task_01())
    journal_modules.debug('run time: {}s'.format(time.time() - start_run_time))
