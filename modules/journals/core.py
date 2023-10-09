# coding: utf8
""" 
@ File: core.py
@ Editor: PyCharm
@ Author: Austin (From Chengdu.China) https://fairy.host
@ HomePage: https://github.com/AustinFairyland
@ OS: Windows 11 Professional Workstation 22H2
@ CreatedTime: 2023-09-11
"""

import sys
import warnings

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')

from loguru import logger
import os


class JournalsModule:

    def __init__(self):
        self.__config_logger()

    def __config_logger(self):
        from utils.publics import PublicUtilsStaticClass
        logs_path = PublicUtilsStaticClass.path_root_conver_system_separator(os.path.join(PublicUtilsStaticClass.path_root, 'logs/services.log'))
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
