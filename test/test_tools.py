# coding: utf8
""" 
@ File: test_tools.py
@ Editor: PyCharm
@ Author: Austin (From Chengdu.China)
@ HomePage: https://github.com/AceProfessional
@ OS: Windows 11 Professional Workstation 22H2
@ CreatedTime: 2023-09-10
"""

import sys
import warnings

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')

import os

from tools.processing_data import TestStaticClass
from utils.public_utils import PublicUtilsStaticClass
from modules.journals import JournalsModule


def test():
    data_a_path = PublicUtilsStaticClass.path_root_conver_system_separator(os.path.join(PublicUtilsStaticClass.path_root(), 'data/temp/pubmed/data.csv'))
    data_b_path = PublicUtilsStaticClass.path_root_conver_system_separator(os.path.join(PublicUtilsStaticClass.path_root(), 'data/temp/pubmed_DB/data.csv'))
    return TestStaticClass.merge_csv_row(file_a=data_a_path, file_b=data_b_path, merge_csv_path='data/temp/new_merge_data.csv')


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
