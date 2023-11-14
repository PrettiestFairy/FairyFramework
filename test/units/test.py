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


class TestClass(PublicToolsBaseClass):

    def __init__(self):
        super().__init__()
        self.config_cls = ConfigClass()

    def test_task_01(self) -> dict:
        print(self._root_path, type(self._root_path))
        print(self.config_cls.config)
        return 'test_task_01 测试完成'

    def test_task_02(self):
        pass


if __name__ == '__main__':
    start_run_time = time.time()
    t_cls = TestClass()
    JournalsModuleClass.debug(t_cls.test_task_01())
    JournalsModuleClass.debug('run time: {}s'.format(time.time() - start_run_time))
