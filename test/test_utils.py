# coding: utf8
""" 
@ File: test_utils.py
@ Editor: PyCharm
@ Author: Austin (From Chengdu.China)
@ HomePage: https://github.com/AceProfessional
@ OS: Windows 11 Professional Workstation 22H2
@ CreatedTime: 2023-09-09
"""

import sys
import warnings

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')

import os

from utils.publics import PublicUtilsStaticClass

if __name__ == '__main__':
    # public_utils = PublicUtils()
    # root = public_utils.path_root()
    print(PublicUtilsStaticClass.path_root)
    ss = os.path.join(PublicUtilsStaticClass.path_root, 'data/temp/test.txt')
    print('path: {}'.format(ss))
    print('path: {}'.format(PublicUtilsStaticClass.path_root_conver_system_separator(sys_path=ss)))
    print('Done')
