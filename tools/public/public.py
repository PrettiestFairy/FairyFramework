# coding: utf8
""" 
@ File: _source.py
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


class PublicToolsBase:
    """公共工具基类"""

    root_path = os.path.abspath(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    )

    @staticmethod
    def api_results():
        results = {"status": "failure", "code": 500, "data": None}
        return results

    @staticmethod
    def data_string():
        results = str()
        return results

    @staticmethod
    def data_integer():
        results = int()
        return results

    @staticmethod
    def data_float():
        results = float()
        return results

    @staticmethod
    def data_boolean():
        results = bool()
        return results

    @staticmethod
    def data_list():
        results = list()
        return results

    @staticmethod
    def data_tuple():
        results = tuple()
        return results

    @staticmethod
    def data_set():
        results = set()
        return results

    @staticmethod
    def data_dict():
        results = dict()
        return results

    @staticmethod
    def data_none():
        return None

    @staticmethod
    def data_byte():
        results = bytes()
        return results

    @staticmethod
    def data_bytearray():
        results = bytearray()
        return results

    @staticmethod
    def data_complex():
        results = complex()
        return results
