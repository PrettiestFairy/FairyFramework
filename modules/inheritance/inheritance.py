# coding: utf8
""" 
@File: inheritance.py
@Editor: PyCharm
@Author: Austin (From Chengdu.China) https://fairy.host
@HomePage: https://github.com/AustinFairyland
@OperatingSystem: Windows 11 Professional Workstation 23H2 Canary Channel
@CreatedTime: 2024-01-04
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

import time
import random

from tools.public import PublicToolsBase
from modules.journals import Journal
from modules.configuration import Config


class Base(Config, Journal, PublicToolsBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
