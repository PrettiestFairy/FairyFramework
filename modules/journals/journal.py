# coding: utf8
""" 
@ File: Journal.py
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
warnings.filterwarnings("ignore")
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from loguru import logger
import threading

from tools.public import PublicToolsBase


class JournalModules:
    """Log Module Class"""

    __logs_path = os.path.normpath(
        os.path.join(PublicToolsBase.root_path, "logs/services.log")
    )
    logger.remove()
    logger.add(
        sink=__logs_path,
        rotation="10 MB",
        retention="180 days",
        format="[{time:YYYY-MM-DD HH:mm:ss} | {elapsed} | {level:<8}]: {message}",
        compression="gz",
        encoding="utf-8",
        # level: TRACE, DEBUG, INFO, SUCCESS, WARNING, ERROR, CRITICAL
        level="DEBUG",
        enqueue=True,
        colorize=True,
        backtrace=True,
    )
    __logs = logger

    @classmethod
    def debug(cls, msg, *args, **kwargs):
        return cls.__logs.debug(msg, *args, **kwargs)

    # @property
    # def catch(self):
    #     """
    #     Inherits the catch method from loguru.
    #     @return: loguru.logger.catch
    #     """
    #     return self.__logs.catch()
    # 
    # def trace(self, msg, *args, **kwargs):
    #     """
    #     Inherits the trace method from loguru.
    #     @param msg: Log messages: String
    #     @param args: Tuple
    #     @param kwargs: Dict
    #     @return: loguru.logger.trace
    #     """
    #     return self.__logs.trace(msg, *args, **kwargs)
    # 
    # def debug(self, msg, *args, **kwargs):
    #     """
    #     Inherits the debug method from loguru.logger.
    #     @param msg: Debug Log messages: String
    #     @param args: Tuple
    #     @param kwargs: Dict
    #     @return: loguru.logger.debug
    #     """
    #     return self.__logs.debug(msg, *args, **kwargs)
    # 
    # def info(self, msg, *args, **kwargs):
    #     """
    #     Inherits the info method from loguru.
    #     @param msg: Info Log messages: String
    #     @param args: Tuple
    #     @param kwargs: Dict
    #     @return: loguru.logger.info
    #     """
    #     return self.__logs.info(msg, *args, **kwargs)
    # 
    # def success(self, msg, *args, **kwargs):
    #     """
    #     Inherits the success method from loguru.
    #     @param msg: Success Log messages: String
    #     @param args: Tuple
    #     @param kwargs: Dict
    #     @return: loguru.logger.success
    #     """
    #     return self.__logs.success(msg, *args, **kwargs)
    # 
    # def warning(self, msg, *args, **kwargs):
    #     """
    #     Inherits the warning method from loguru.
    #     @param msg: Warning Log messages: String
    #     @param args: Tuple
    #     @param kwargs: Dict
    #     @return: loguru.logger.warning
    #     """
    #     return self.__logs.warning(msg, *args, **kwargs)
    # 
    # def error(self, msg, *args, **kwargs):
    #     """
    #     Inherits the error method from loguru.
    #     @param msg: Error Log messages: String
    #     @param args: Tuple
    #     @param kwargs: Dict
    #     @return: loguru.logger.error
    #     """
    #     return self.__logs.error(msg, *args, **kwargs)
    # 
    # def critical(self, msg, *args, **kwargs):
    #     """
    #     Inherits the critical method from loguru.
    #     @param msg: Critical Log messages: String
    #     @param args: Tuple
    #     @param kwargs: Dict
    #     @return: loguru.logger.critical
    #     """
    #     return self.__logs.critical(msg, *args, **kwargs)
    # 
    # def exception(self, msg, *args, **kwargs):
    #     """
    #     Inherits the exception method from loguru.
    #     @param msg: Exception Log messages: String
    #     @param args: Tuple
    #     @param kwargs: Dict
    #     @return: loguru.logger.exception
    #     """
    #     return self.__logs.exception(msg, *args, **kwargs)
