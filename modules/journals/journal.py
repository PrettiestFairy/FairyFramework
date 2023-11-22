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

from loguru import logger
import threading

from tools.publics import PublicToolsBaseClass


class JournalModulesClass(PublicToolsBaseClass):
    """ 日志模块类 """

    __instance_lock = threading.Lock()
    __logger_instance = False

    def __init__(self):
        super(PublicToolsBaseClass, self).__init__()
        self.__logger_instance = True

    def __new__(cls):
        if not cls.__logger_instance:
            with cls.__instance_lock:
                if not cls.__logger_instance:
                    cls.__logger_instance = super(JournalModulesClass, cls).__new__(cls)
                    cls.__logger_instance.__config_logger()
        return cls.__logger_instance.__logs
    
    def __config_logger(self):
        """
        logger 配置
        @return: logger对象: logger object 
        """
        # logs_path = PublicToolsBaseClass.conver_slach(os.path.join(PublicToolsBaseClass.root_path, 'logs/services.log'))
        logs_path = os.path.normpath(os.path.join(self.root_path, 'logs/services.log'))
        logger.add(
            sink=logs_path,
            rotation='10 MB',
            retention='180 days',
            format="[{time:YYYY-MM-DD HH:mm:ss} | {elapsed} | {level:<8}]: {message}",
            compression="gz",
            encoding='utf-8',
            # level='TRACE',
            # level='DEBUG',
            level='INFO',
            enqueue=True,
            # colorize=True,
            backtrace=True,
        )

    @property
    def __logs(self):
        """
        私有方法 logger
        @return: Object logger对象
        """
        return logger

    @property
    def catch(self):
        """
        继承 loguru.logger 的 catch 方法
        @return: Object loguru.logger.catch 方法
        """
        return self.__logs.catch()

    def trace(self, msg, *args, **kwargs):
        """
        继承 loguru.logger 的 trace 方法
        @param msg: String 日志信息
        @param args: args
        @param kwargs: kwargs
        @return: Object loguru.logger.trace 方法
        """
        return self.__logs.trace(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        """
        继承 loguru.logger 的 debug 方法
        @param msg: String 日志信息
        @param args: args
        @param kwargs: kwargs
        @return: Object loguru.logger.debug 方法
        """
        return self.__logs.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        """
        继承 loguru.logger 的 info 方法
        @param msg: String 日志信息
        @param args: args
        @param kwargs: kwargs
        @return: Object loguru.logger.info 方法
        """
        return self.__logs.info(msg, *args, **kwargs)

    def success(self, msg, *args, **kwargs):
        """
        继承 loguru.logger 的 success 方法
        @param msg: String 日志信息
        @param args: args
        @param kwargs: kwargs
        @return: Object loguru.logger.success 方法
        """
        return self.__logs.success(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        """
        继承 loguru.logger 的 warning 方法
        @param msg: String 日志信息
        @param args: args
        @param kwargs: kwargs
        @return: Object loguru.logger.warning 方法
        """
        return self.__logs.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        """
        继承 loguru.logger 的 error 方法
        @param msg: String 日志信息
        @param args: args
        @param kwargs: kwargs
        @return: Object loguru.logger.error 方法
        """
        return self.__logs.error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        """
        继承 loguru.logger 的 critical 方法
        @param msg: String 日志信息
        @param args: args
        @param kwargs: kwargs
        @return: Object loguru.logger.critical 方法
        """
        return self.__logs.critical(msg, *args, **kwargs)

    def exception(self, msg, *args, **kwargs):
        """
        继承 loguru.logger 的 exception 方法
        @param msg: String 日志信息
        @param args: args
        @param kwargs: kwargs
        @return: Object loguru.logger.exception 方法
        """
        return self.__logs.exception(msg, *args, **kwargs)
