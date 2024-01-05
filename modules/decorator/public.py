# coding: utf8
"""
@ File: public.py
@ Editor: PyCharm
@ Author: Austin (From Chengdu.China) https://fairy.host
@ HomePage: https://github.com/AustinFairyland
@ OS: Linux Ubunut 22.04.4 Kernel 6.2.0-36-generic 
@ CreatedTime: 2023/11/25
"""
from __future__ import annotations

import sys
import warnings
import platform
import asyncio

sys.dont_write_bytecode = True
warnings.filterwarnings("ignore")
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import time
from typing import Callable, Mapping

from modules.journals import JournalModulesClass


class TimeDecorators:
    """Runtime Decorator"""

    def __call__(self, function, *args, **kwargs):
        def warpper(*args, **kwargs):
            journal = JournalModulesClass()
            start_time = time.time()
            result = function(*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            journal.debug("{} run {} second".format(function.__name__, elapsed_time))
            return result

        return warpper


class MethodDecorators:
    def __init__(self, annotation):
        self.__annotation = annotation

    @TimeDecorators()
    def __call__(self, function, *args, **kwargs):
        def wrapper(*args, **kwargs):
            results = None
            try:
                journal = JournalModulesClass()
                journal.info("Action Running {}".format(self.__annotation))
                results = function(*args, **kwargs)
                journal.info("Success Running {}".format(self.__annotation))
            except Exception as error:
                journal.info("Failure Running {}".format(self.__annotation))
                journal.error(error)
            return results

        return wrapper
