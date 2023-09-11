# coding: utf8
""" 
@ File: __init__.py
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

from .test import TestStaticClass

TestStaticClass = TestStaticClass()

__all__ = [
    TestStaticClass
]
