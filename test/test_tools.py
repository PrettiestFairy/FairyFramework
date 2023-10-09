# coding: utf8
""" 
@ File: test_tools.py
@ Editor: PyCharm
@ Author: Austin (From Chengdu.China) https://fairy.host
@ HomePage: https://github.com/AustinFairyland
@ OS: Windows 11 Professional Workstation 22H2
@ CreatedTime: 2023-09-10
"""

import sys
import warnings

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')

import os

from tools.data import TestStaticClass
from utils.publics import PublicUtilsStaticClass
from modules.journals import JournalsModule


def test():
    JournalsModule.debug('项目根路径: {}'.format(PublicUtilsStaticClass.path_root))
    test_path = os.path.join(PublicUtilsStaticClass.path_root, 'data/temp/test.txt')
    JournalsModule.debug('修改前路径格式: {}'.format(test_path))
    JournalsModule.debug('修改后路径格式: {}'.format(PublicUtilsStaticClass.path_root_conver_system_separator(test_path)))
    data_a_path = PublicUtilsStaticClass.path_root_conver_system_separator(os.path.join(PublicUtilsStaticClass.path_root, 'data/temp/file_a.csv'))
    data_b_path = PublicUtilsStaticClass.path_root_conver_system_separator(os.path.join(PublicUtilsStaticClass.path_root, 'data/temp/file_b.csv'))
    JournalsModule.debug(TestStaticClass.merge_csv_row(file_a=data_a_path, file_b=data_b_path, merge_csv_path='data/temp/new_merge_file.csv'))
    return True


def journals_module():
    JournalsModule.trace('跟踪日志')
    JournalsModule.debug('调试日志')
    JournalsModule.info('信息日志')
    JournalsModule.success('成功日志')
    JournalsModule.warning('警告日志')
    JournalsModule.error('错误日志')
    JournalsModule.critical('重要日志')


if __name__ == '__main__':
    print(test())
