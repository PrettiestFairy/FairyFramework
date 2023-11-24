# coding: utf8
""" 
@ File: public.py
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


class PublicToolsBaseClass:
    """公共工具基类"""

    def __init__(self):
        self.__root_path = os.path.abspath(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        )
        self.__api_results = {"status": "failure", "code": 500, "data": None}
        self.__data_string = str()
        self.__data_integer = int()
        self.__data_float = float()
        self.__data_boolean = bool()
        self.__data_list = list()
        self.__data_tuple = tuple()
        self.__data_set = set()
        self.__data_dict = dict()
        self.__data_none = None
        self.__data_byte = bytes()
        self.__data_bytearray = bytearray()
        self.__data_complex = complex()

    @property
    def root_path(self) -> str:
        """
        项目根路径
        :return: 项目根路径: str
        """
        return self.__root_path

    @property
    def api_result(self):
        return self.__api_results

    @property
    def data_string(self):
        return self.__data_string

    @property
    def data_integer(self):
        return self.__data_integer

    @property
    def data_float(self):
        return self.__data_float

    @property
    def data_boolean(self):
        return self.__data_boolean

    @property
    def data_list(self):
        return self.__data_list

    @property
    def data_tuple(self):
        return self.__data_tuple

    @property
    def data_set(self):
        return self.__data_set

    @property
    def data_dict(self):
        return self.__data_dict

    @property
    def data_none(self):
        return self.__data_none

    @property
    def data_byte(self):
        return self.__data_byte

    @property
    def data_bytearray(self):
        return self.__data_bytearray

    @property
    def data_complex(self):
        return self.__data_complex
