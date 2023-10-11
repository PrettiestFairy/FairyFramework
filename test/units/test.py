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
warnings.filterwarnings('ignore')
if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import time
import random

from utils.publics import PublicUtilsBaseClass
from modules.journals import JournalsModuleClass


class TestClass:

    def __init__(self):
        self.public_utils_base_cls = PublicUtilsBaseClass()
        self.journals_module_cls = JournalsModuleClass()

    def test_task_01(self) -> dict:
        r_path = self.public_utils_base_cls.root_path
        logs_dir_path = self.public_utils_base_cls.conver_slach(os.path.join(r_path, 'logs/services.log'))
        return {
            'root': r_path,
            'logs': logs_dir_path
        }

    def test_task_02(self):
        pass


if __name__ == '__main__':
    start_run_time = time.time()
    t_cls = TestClass()
    t_cls.journals_module_cls.debug(t_cls.test_task_01())
    t_cls.journals_module_cls.debug('run time: {}s'.format(time.time() - start_run_time))
