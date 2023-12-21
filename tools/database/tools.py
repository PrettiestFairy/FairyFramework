# coding: utf8
"""
@ File: tools.py
@ Editor: PyCharm
@ Author: Austin (From Chengdu.China) https://fairy.host
@ HomePage: https://github.com/AustinFairyland
@ OS: Linux Ubunut 22.04.4 Kernel 6.2.0-36-generic 
@ CreatedTime: 2023/12/21
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


class SQLStatement:
    @staticmethod
    def filter_join(filter_name, field_name, field_value, field_operation):
        if not isinstance(field_name, str):
            raise TypeError
        if isinstance(field_value, str):
            if field_operation in ("like", "ilike"):
                results = "{} {} {} '%{}%'".format(
                    filter_name, field_name, field_operation, field_value
                )
            else:
                results = "{} {} {} '{}'".format(
                    filter_name, field_name, field_operation, field_value
                )
        else:
            if field_operation in ("like", "ilike"):
                raise SyntaxError
            else:
                results = "{} {} {} '{}'".format(
                    filter_name, field_name, field_operation, field_value
                )
        return results

    @staticmethod
    def where_clause(filter_iterable):
        if not isinstance(filter_iterable, (list, tuple, set)):
            raise TypeError
        results = " ".join(filter_iterable)
        return results
