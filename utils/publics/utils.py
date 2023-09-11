# coding: utf8
""" 
@ File: utils.py
@ Editor: PyCharm
@ Author: Austin (From Chengdu.China)
@ HomePage: https://github.com/AceProfessional
@ OS: Windows 11 Professional Workstation 22H2
@ CreatedTime: 2023-09-11
"""

import sys
import warnings

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')

import os
import platform


class PublicUtilsStaticClass:

    def __init__(self):
        pass

    @property
    def path_root(self) -> str:
        """
        项目根路径
        :return: 项目根路径
        """
        return os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

    @staticmethod
    def path_root_conver_system_separator(sys_path: str) -> str:
        """
        转换路径分隔符为系统分隔符
        :param sys_path: 系统路径
        :return: 系统路径
        """
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
