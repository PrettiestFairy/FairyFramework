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
warnings.filterwarnings("ignore")
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from dotenv import load_dotenv
import yaml

from modules.journals import JournalModulesClass
from tools.public import PublicToolsBaseClass
from tools.public import ReadFilesError


class BaseConfigClass:
    """Base Configuration Base Class"""

    def __init__(self, *args, **kwargs):
        self._journal = JournalModulesClass()
        self._public_tools = PublicToolsBaseClass()

    def __get_config_path(self) -> str:
        """
        Get the path to the configuration file
        @return: Path to the configuration file: String
        """
        config_path = os.path.normpath(os.path.join(self._public_tools.root_path, "config.yaml"))
        if not os.path.isfile(config_path):
            config_path = os.path.normpath(
                os.path.join(self._public_tools.root_path, "../../conf/config.dev.yaml")
            )
            if not os.path.isfile(config_path):
                config_path = os.path.normpath(
                    os.path.join(self._public_tools.root_path, "conf/config.yaml")
                )
                if not os.path.isfile(config_path):
                    config_path = os.path.normpath(
                        os.path.join(self._public_tools.root_path, "conf/config.dev.yaml")
                    )
        try:
            if os.path.isfile(config_path):
                return config_path
            else:
                raise ReadFilesError("Config file load error.")
        except Exception as error:
            self.exception(error)
            sys.exit(1)

    @property
    def __config_path(self):
        self._journal.info("Config File: {}".format(self.__get_config_path()))
        return self.__get_config_path()

    def __base_config(self) -> dict:
        """
        Getting configuration information
        @return: configuration information: String
        """

        try:
            with open(self.__config_path, "r", encoding="utf8") as file:
                read_config = yaml.safe_load(file)
            return read_config
        except Exception as error:
            self._journal.exception(error)

    @property
    def _base_config(self) -> dict:
        return self.__base_config()


class DevelopmentConfigClass(BaseConfigClass):
    """Development Environment Configuration"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _development_config(self) -> dict:
        return self._base_config.get("Development")


class TestConfigClass(BaseConfigClass):
    """Test Environment Configuration"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _test_config(self) -> dict:
        return self._base_config.get("Test")


class ProductionConfigClass(BaseConfigClass):
    """Production Environment Configuration"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _production_config(self) -> dict:
        return self._base_config.get("Production")


class ConfigClass(DevelopmentConfigClass, TestConfigClass, ProductionConfigClass):
    """Configuration"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        load_dotenv()
        try:
            self.__run_env: str = os.getenv("RUN_ENVIRONMENT")
            if self.__run_env is None:
                self.__run_env = "dev"
                self._journal.warning(
                    "Configuration environment configuration error"
                    "Default with the development environment."
                )
        except Exception as error:
            self._journal.exception(error)
            sys.exit(1)

    def __development(self) -> dict:
        return self._development_config()

    def __test(self) -> dict:
        return self._test_config()

    def __production(self) -> dict:
        return self._production_config()

    @property
    def config(self) -> dict:
        try:
            self._journal.info("operating environment：{}".format(self.__run_env))
            if self.__run_env.lower() in ["production", "prod", "pro", "p"]:
                return self.__production()
            elif self.__run_env.lower() in ["test", "t"]:
                return self.__test()
            else:
                return self.__development()
        except Exception as error:
            self._journal.exception(error)
            return self.data_dict
