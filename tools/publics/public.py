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


class PublicToolsBaseClass:
    """ 公共工具基类 """

    def __init__(self):
        pass

    @property
    def root_path(self) -> str:
        """
        项目根路径
        :return: 项目根路径: str
        """
        return os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

    def conver_slach(self, sys_path: str, paths: str = None) -> str:
        """
        转换路径分隔符为系统分隔符
        :param sys_path: String 系统路径
        :param paths: String 路径
        :return: String 转换为系统分隔符后的系统路径
        """
        if paths is not None:
            sys_path = os.path.join(sys_path, paths)
        if platform.system() == 'Windows':
            separator = '\\'
        else:
            separator = '/'
        new_path = ''
        for a in sys_path.split('/'):
            if '\\' in a:
                for b in a.split('\\'):
                    new_path += b + separator
            else:
                new_path += a + separator

        return new_path[:-1]
