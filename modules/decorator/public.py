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

from modules.journals import InitJournalModulesClass


class TimingDecorator:
    """Runtime Decorator"""

    def __call__(self, func, *args, **kwargs):
        def warpper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            InitJournalModulesClass.journal.debug(
                "{} run {} second".format(func.__name__, elapsed_time)
            )
            return result

        return warpper


class MethodRunningAnnotateDecorator:
    def __init__(self, annotate: str, *args, **kwargs):
        self.annotate: str = annotate

    @InitJournalModulesClass.journal.catch()
    def __call__(self, method: Callable[..., ...], *args, **kwargs):
        def warpper(*args, **kwargs):
            try:
                InitJournalModulesClass.journal.info("")
                warpper(*args, **kwargs)
                InitJournalModulesClass.journal.success("")
            except Exception as error:
                print(error)
                InitJournalModulesClass.journal.error("")

        return warpper


class MethodDecorators:
    def __init__(self, annotation):
        self.__annotation = annotation

    @TimingDecorator()
    def __call__(self, function, *args, **kwargs):
        def wrapper(*args, **kwargs):
            print("Start Running {}".format(self.__annotation))
            results = None
            try:
                results = function(*args, **kwargs)
            except Exception as error:
                print(error)
            return results

        return wrapper


@MethodDecorators("123")
def run():
    # print("run...")
    return True


if __name__ == "__main__":
    print(run())
