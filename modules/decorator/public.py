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
from modules.journals import InitJournalModulesClass


class TimingDecorator:
    """Runtime Decorator"""

    def __call__(self, func):
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
