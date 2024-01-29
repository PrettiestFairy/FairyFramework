# coding: utf8
""" 
@File: _configurations.py
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
warnings.filterwarnings("ignore")
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from dotenv import load_dotenv
import yaml

from modules.journals import Journal
from tools.public import PublicToolsBase
from tools.abnormal import ReadFileError


class BaseConfigClass:
    """Base Configuration Base Class"""

    @staticmethod
    def __get_config_path() -> str:
        """
        Get the path to the configuration file
        @return: Path to the configuration file: String
        """
        config_path = os.path.normpath(
            os.path.join(PublicToolsBase.root_path, "config.yaml")
        )
        if not os.path.isfile(config_path):
            config_path = os.path.normpath(
                os.path.join(PublicToolsBase.root_path, "../../conf/config.dev.yaml")
            )
            if not os.path.isfile(config_path):
                config_path = os.path.normpath(
                    os.path.join(PublicToolsBase.root_path, "conf/config.yaml")
                )
                if not os.path.isfile(config_path):
                    config_path = os.path.normpath(
                        os.path.join(PublicToolsBase.root_path, "conf/config.dev.yaml")
                    )
        try:
            if os.path.isfile(config_path):
                return config_path
            else:
                raise ReadFileError("Config file load error.")
        except Exception as error:
            Journal.error(error)
            sys.exit(1)

    @classmethod
    def _base_config(cls) -> dict:
        """
        Getting configuration information
        @return: configuration information: String
        """
        __config_path = cls.__get_config_path()
        Journal.info("Config File: {}".format(__config_path))
        try:
            with open(__config_path, "r", encoding="utf8") as file:
                read_config = yaml.safe_load(file)
            return read_config
        except Exception as error:
            Journal.error(error)


class DevelopmentConfigClass(BaseConfigClass):
    """Development Environment Configuration"""

    @classmethod
    def _development_config(cls) -> dict:
        return cls._base_config().get("Development")


class TestConfigClass(BaseConfigClass):
    """Test Environment Configuration"""

    @classmethod
    def _test_config(cls) -> dict:
        return cls._base_config().get("Test")


class ProductionConfigClass(BaseConfigClass):
    """Production Environment Configuration"""

    @classmethod
    def _production_config(cls) -> dict:
        return cls._base_config().get("Production")


class Config(DevelopmentConfigClass, TestConfigClass, ProductionConfigClass):
    """Configuration"""

    @classmethod
    def __run_env(cls):
        try:
            load_dotenv()
            __run_env: str = os.getenv("RUN_ENVIRONMENT")
            if __run_env is None:
                __run_env = "dev"
                Journal.warning(
                    "Configuration environment configuration error "
                    "Default with the development environment."
                )
        except Exception as error:
            Journal.error(error)
            sys.exit(1)
        return __run_env

    @classmethod
    def __development(cls) -> dict:
        return cls._development_config()

    @classmethod
    def __test(cls) -> dict:
        return cls._test_config()

    @classmethod
    def __production(cls) -> dict:
        return cls._production_config()

    @classmethod
    def config(cls) -> dict:
        try:
            __run_env = cls.__run_env()
            Journal.info("Operating environment：{}".format(__run_env))
            if __run_env.lower() in ["production", "prod", "pro", "p"]:
                return cls.__production()
            elif __run_env.lower() in ["test", "t"]:
                return cls.__test()
            else:
                return cls.__development()
        except Exception as error:
            Journal.error(error)
            return PublicToolsBase.data_dict()


config = Config.config()
