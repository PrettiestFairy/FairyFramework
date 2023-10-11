# coding: utf8
""" 
@File: configurations.py
@Editor: PyCharm
@Author: Austin (From Chengdu.China) https://fairy.host
@HomePage: https://github.com/AustinFairyland
@OperatingSystem: Windows 11 Professional Workstation 23H2 Canary Channel
@CreatedTime: 2023-10-11
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

from dotenv import load_dotenv
import yaml

from utils.publics import PublicUtilsBaseClass
from modules.journals import JournalsModuleClass


class BaseConfigClass:
    """ 基础配置基类 """

    def __init__(self):
        self.__config_path = self.__get_config_path()

    def __get_config_path(self) -> str:
        config_path = PublicUtilsBaseClass.conver_slach(PublicUtilsBaseClass.root_path, 'config.yaml')
        if not os.path.isfile(config_path):
            config_path = PublicUtilsBaseClass.conver_slach(PublicUtilsBaseClass.root_path, 'config.dev.yaml')
            if not os.path.isfile(config_path):
                config_path = PublicUtilsBaseClass.conver_slach(PublicUtilsBaseClass.root_path, 'conf/config.yaml')
                if not os.path.isfile(config_path):
                    config_path = PublicUtilsBaseClass.conver_slach(PublicUtilsBaseClass.root_path, 'conf/config.dev.yaml')
        try:
            if os.path.isfile(config_path):
                JournalsModuleClass.info('配置文件：{}'.format(config_path))
                return config_path
            else:
                raise Exception('配置文件加载失败')
        except Exception as error:
            JournalsModuleClass.exception(error)

    def __base_config(self) -> dict:
        """
        获取配置信息
        :return: dict 配置信息
        """
        try:
            with open(self.__config_path, 'r', encoding='utf8') as file:
                read_config = yaml.safe_load(file)
                JournalsModuleClass.info('配置文件读取成功：{}'.format(self.__config_path))
            return read_config
        except Exception as error:
            JournalsModuleClass.exception(error)

    @property
    def _base_config(self) -> dict:
        return self.__base_config()


class DevelopmentConfigClass(BaseConfigClass):
    """ 开发环境配置 """

    def __init__(self):
        super().__init__()

    def _development_config(self) -> dict:
        return self._base_config.get('Development')


class TestConfigClass(BaseConfigClass):
    """ 测试环境配置 """

    def __init__(self):
        super().__init__()

    def _test_config(self) -> dict:
        return self._base_config.get('Test')


class ProductionConfigClass(BaseConfigClass):
    """ 生产环境配置 """

    def __init__(self):
        super().__init__()

    def _production_config(self) -> dict:
        return self._base_config.get('Production')


class ConfigClass(DevelopmentConfigClass, TestConfigClass, ProductionConfigClass):

    def __init__(self):
        super().__init__()
        load_dotenv()
        try:
            self.__run_env: str = os.getenv('RUN_ENVIRONMENT')
            if self.__run_env is None:
                self.__run_env = 'dev'
                JournalsModuleClass.warning('配置环境配置错误，默认使用开发环境启动项目')
            JournalsModuleClass.info('项目运行环境：{}'.format(self.__run_env))
        except Exception as error:
            JournalsModuleClass.exception(error)

    def __development(self) -> dict:
        return self._development_config()

    def __test(self) -> dict:
        return self._test_config()

    def __production(self) -> dict:
        return self._production_config()

    @property
    def config(self) -> dict:
        try:
            if self.__run_env.lower() in ['production', 'prod', 'pro', 'p']:
                return self.__production()
            elif self.__run_env.lower() in ['test', 't']:
                return self.__test()
            else:
                return self.__development()
        except Exception as error:
            JournalsModuleClass.exception(error)
