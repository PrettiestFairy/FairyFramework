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

import time

from tools.publics import PublicToolsBaseClass
from modules.journals import JournalsModuleClass
from conf import ConfigClass
from tools.database import MySQLStandaloneToolsClass
from tools.database import MySQLMasterSlaveDBRouterToolsClass
from tools.middleware import RedisStandaloneToolsClass


class TestClass:

    def __init__(self):
        pass

    def test_task_01(self) -> dict:
        r_path = PublicToolsBaseClass.root_path
        logs_dir_path = PublicToolsBaseClass.conver_slach(r_path, paths='logs/services.log')
        config = ConfigClass.config
        JournalsModuleClass.info('运行配置：{}'.format(config))
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
        _redis = RedisStandaloneToolsClass()
        _redis.redis_set('code', 1234)
        d = _redis.redis_get('code')
        return 'test_task_01 测试完成'

    def test_task_02(self):
        pass


if __name__ == '__main__':
    start_run_time = time.time()
    t_cls = TestClass()
    JournalsModuleClass.debug(t_cls.test_task_01())
    JournalsModuleClass.debug('run time: {}s'.format(time.time() - start_run_time))
