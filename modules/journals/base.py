# coding: utf8
""" 
@ File: base.py
@ Editor: PyCharm
@ Author: Austin (From Chengdu.China) https://fairy.host
@ HomePage: https://github.com/AustinFairyland
@ OS: Windows 11 Professional Workstation 22H2
@ CreatedTime: 2023-09-11
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

from loguru import logger

from utils.publics import PublicUtilsBaseClass


class JournalsModuleClass:
    """日志模块类"""

    def __init__(self):
        self.__config_logger()

    def __config_logger(self):
        logs_path = PublicUtilsBaseClass.conver_slach(os.path.join(PublicUtilsBaseClass.root_path, 'logs/services.log'))
        logger.add(
            sink=logs_path,
            rotation='10 MB',
            retention='180 days',
            format="[{time:YYYY-MM-DD HH:mm:ss} | {elapsed} | {level:<8}]: {message}",
            compression="gz",
            encoding='utf-8',
            # level='TRACE',
            level='DEBUG',
            enqueue=True,
            # colorize=True,
            backtrace=True,
        )

    @property
    def __logs(self):
        return logger

    def catch(self):
        return self.__logs.catch()

    def trace(self, msg, *args, **kwargs):
        return self.__logs.trace(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        return self.__logs.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        return self.__logs.info(msg, *args, **kwargs)

    def success(self, msg, *args, **kwargs):
        return self.__logs.success(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        return self.__logs.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        return self.__logs.error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        return self.__logs.critical(msg, *args, **kwargs)

    def exception(self, msg, *args, **kwargs):
        return self.__logs.exception(msg, *args, **kwargs)
