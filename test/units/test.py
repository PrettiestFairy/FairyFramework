# coding: utf8
""" 
@File: test.py
@Editor: PyCharm
@Author: Austin (From Chengdu.China) https://fairy.host
@HomePage: https://github.com/AustinFairyland
@OperatingSystem: Windows 11 Professional Workstation 23H2 Canary Channel
@CreatedTime: 2023-10-11
"""
from __future__ import annotations

import sys
import warnings
import platform
import asyncio

sys.dont_write_bytecode = True
warnings.filterwarnings("ignore")
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import time

from tools.publics import PublicToolsBaseClass
from modules.journals import InitJournalModulesClass
from conf import InitConfigClass
from modules.decorator import TimingDecorator
from tools.publics import InitDateTimeClass


class TestClass(PublicToolsBaseClass):
    def __init__(self):
        super(PublicToolsBaseClass, self).__init__()

    @TimingDecorator()
    def test_task_01(self):
        def __kv(items):
            if isinstance(items, dict):
                for key, value in items.items():
                    if isinstance(value, dict):
                        InitJournalModulesClass.journal.debug((key, value))
                        __kv(value)
                    else:
                        InitJournalModulesClass.journal.debug((key, value))

        InitJournalModulesClass.journal.info("Start Test Task")
        InitJournalModulesClass.journal.debug("Config")
        for key, value in InitConfigClass.config.config.items():
            if isinstance(value, dict):
                InitJournalModulesClass.journal.debug((key, value))
                __kv(value)
            else:
                InitJournalModulesClass.journal.debug((key, value))

        InitJournalModulesClass.journal.success("Tast Task Done")
        return True

    @TimingDecorator()
    def test2(self):
        InitJournalModulesClass.journal.debug(
            (
                InitDateTimeClass.datetimes.normtimestamp(),
                InitDateTimeClass.datetimes.normdatetime(),
                len(InitDateTimeClass.datetimes.normtimestamp().__str__()),
                InitDateTimeClass.datetimes.timestamp_nbit(20),
                InitDateTimeClass.datetimes.timestamp_dt("2023-01-01 00:00:00"),
                InitDateTimeClass.datetimes.datetime_ts(1672502400),
            )
        )


def main(*args, **kwargs):
    tcls = TestClass()

    # tcls.test_task_01()
    tcls.test2()


if __name__ == "__main__":
    main()
