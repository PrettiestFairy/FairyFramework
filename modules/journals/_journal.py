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
from typing import overload

from tools.public import PublicToolsBase


class Journal:
    """Log Module Class"""

    __logs_path = os.path.normpath(
        os.path.join(PublicToolsBase.root_path, "logs/services.log")
    )
    logger.remove()
    logger.add(
        sink=__logs_path,
        rotation="10 MB",
        retention="60 days",
        # format="[{time:YYYY-MM-DD HH:mm:ss} | {elapsed} | {level:<8}]: {message}",
        format="[{time:YYYY-MM-DD HH:mm:ss} | {level:<8}]: {message}",
        compression="gz",
        encoding="utf-8",
        # level: TRACE, DEBUG, INFO, SUCCESS, WARNING, ERROR, CRITICAL
        level="INFO",
        enqueue=True,
        colorize=True,
        backtrace=True,
    )
    logger.add(
        sink=sys.stdout,
        format="[<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level:<8}</level>]: {message}",
        level="TRACE",
        colorize=True,
    )
    __logs = logger
    __logs.critical(
        """
                                                                高山仰止,景行行止.虽不能至,心向往之。  
                                      ___              __  _          ______                                             __  
                                     /   | __  _______/ /_(_)___     / ____/________ _____ ___  ___ _      ______  _____/ /__
                                    / /| |/ / / / ___/ __/ / __ \   / /_  / ___/ __ `/ __ `__ \/ _ \ | /| / / __ \/ ___/ //_/
                                   / ___ / /_/ (__  ) /_/ / / / /  / __/ / /  / /_/ / / / / / /  __/ |/ |/ / /_/ / /  / ,<   
                                  /_/  |_\__,_/____/\__/_/_/ /_/  /_/   /_/   \__,_/_/ /_/ /_/\___/|__/|__/\____/_/  /_/|_|  
                                  
                                                                   江城子 . 程序员之歌
                                                                  
                                                               十年生死两茫茫，写程序，到天亮。
                                                                   千行代码，Bug何处藏。
                                                               纵使上线又怎样，朝令改，夕断肠。
                                                               
                                                               领导每天新想法，天天改，日日忙。
                                                                   相顾无言，惟有泪千行。
                                                               每晚灯火阑珊处，夜难寐，加班狂。
        """
    )

    @classmethod
    def trace(cls, msg, *args, **kwargs):
        """
        Inherits the trace method from loguru.
        @param msg: Log messages: String
        @param args: Tuple
        @param kwargs: Dict
        @return: loguru.logger.trace
        """
        return cls.__logs.trace(msg, *args, **kwargs)

    @classmethod
    def debug(cls, msg, *args, **kwargs):
        """
        Inherits the debug method from loguru.logger
        @param msg: Debug Log messages: String
        @param args: Tuple
        @param kwargs: Dict
        @return: loguru.logger.debug
        """
        return cls.__logs.debug(msg, *args, **kwargs)

    @classmethod
    def info(cls, msg, *args, **kwargs):
        """
        Inherits the info method from loguru.
        @param msg: Info Log messages: String
        @param args: Tuple
        @param kwargs: Dict
        @return: loguru.logger.info
        """
        return cls.__logs.info(msg, *args, **kwargs)

    @classmethod
    def success(cls, msg, *args, **kwargs):
        """
        Inherits the success method from loguru.
        @param msg: Success Log messages: String
        @param args: Tuple
        @param kwargs: Dict
        @return: loguru.logger.success
        """
        return cls.__logs.success(msg, *args, **kwargs)

    @classmethod
    def warning(cls, msg, *args, **kwargs):
        """
        Inherits the warning method from loguru.
        @param msg: Warning Log messages: String
        @param args: Tuple
        @param kwargs: Dict
        @return: loguru.logger.warning
        """
        return cls.__logs.warning(msg, *args, **kwargs)

    @classmethod
    def error(cls, msg, *args, **kwargs):
        """
        Inherits the error method from loguru.
        @param msg: Error Log messages: String
        @param args: Tuple
        @param kwargs: Dict
        @return: loguru.logger.error
        """
        return cls.__logs.error(msg, *args, **kwargs)

    @classmethod
    def critical(cls, msg, *args, **kwargs):
        """
        Inherits the critical method from loguru.
        @param msg: Critical Log messages: String
        @param args: Tuple
        @param kwargs: Dict
        @return: loguru.logger.critical
        """
        return cls.__logs.critical(msg, *args, **kwargs)

    @classmethod
    def exception(cls, msg, *args, **kwargs):
        """
        Inherits the exception method from loguru.
        @param msg: Exception Log messages: String
        @param args: Tuple
        @param kwargs: Dict
        @return: loguru.logger.exception
        """
        return cls.__logs.exception(msg, *args, **kwargs)
