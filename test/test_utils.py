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

from utils.public_utils import PublicUtils

if __name__ == '__main__':
    public_utils = PublicUtils()
    root = public_utils.path_root()
    print(root)
