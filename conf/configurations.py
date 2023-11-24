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

from tools.publics import PublicToolsBaseClass
from tools.publics import ReadFilesError
from modules.journals import JournalModulesClass

Journal = JournalModulesClass()


class BaseConfigClass(PublicToolsBaseClass):
    """Base Configuration Base Class"""

    def __init__(self):
        super(PublicToolsBaseClass, self).__init__()
        self.__config_path = self.__get_config_path()

    def __get_config_path(self) -> str:
        """
        Get the path to the configuration file
        @return: Path to the configuration file: String
        """
        config_path = os.path.normpath(os.path.join(self.root_path, "config.yaml"))
        if not os.path.isfile(config_path):
            config_path = os.path.normpath(
                os.path.join(self.root_path, "config.dev.yaml")
            )
            if not os.path.isfile(config_path):
                config_path = os.path.normpath(
                    os.path.join(self.root_path, "conf/config.yaml")
                )
                if not os.path.isfile(config_path):
                    config_path = os.path.normpath(
                        os.path.join(self.root_path, "conf/config.dev.yaml")
                    )
        try:
            if os.path.isfile(config_path):
                Journal.info("Config File: {}".format(config_path))
                return config_path
            else:
                raise ReadFilesError("Config file load error.")
        except Exception as error:
            Journal.exception(error)
            sys.exit(1)

    def __base_config(self) -> dict:
        """
        Getting configuration information
        @return: configuration information: String
        """

        try:
            with open(self.__config_path, "r", encoding="utf8") as file:
                read_config = yaml.safe_load(file)
                Journal.info("configuration file：{}".format(self.__config_path))
            return read_config
        except Exception as error:
            Journal.exception(error)

    @property
    def _base_config(self) -> dict:
        return self.__base_config()


class DevelopmentConfigClass(BaseConfigClass):
    """Development Environment Configuration"""

    def __init__(self):
        super(BaseConfigClass, self).__init__()

    def _development_config(self) -> dict:
        return self._base_config.get("Development")


class TestConfigClass(BaseConfigClass):
    """Test Environment Configuration"""

    def __init__(self):
        super(BaseConfigClass, self).__init__()

    def _test_config(self) -> dict:
        return self._base_config.get("Test")


class ProductionConfigClass(BaseConfigClass):
    """Production Environment Configuration"""

    def __init__(self):
        super(BaseConfigClass, self).__init__()

    def _production_config(self) -> dict:
        return self._base_config.get("Production")


class ConfigClass(DevelopmentConfigClass, TestConfigClass, ProductionConfigClass):
    """Configuration"""

    def __init__(self):
        super(DevelopmentConfigClass, self).__init__()
        super(TestConfigClass, self).__init__()
        super(ProductionConfigClass, self).__init__()
        load_dotenv()
        try:
            self.__run_env: str = os.getenv("RUN_ENVIRONMENT")
            if self.__run_env is None:
                self.__run_env = "dev"
                Journal.warning("Configuration environment configuration error")
                Journal.warning("Default with the development environment")
            Journal.info("operating environment：{}".format(self.__run_env))
        except Exception as error:
            Journal.exception(error)
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
            if self.__run_env.lower() in ["production", "prod", "pro", "p"]:
                return self.__production()
            elif self.__run_env.lower() in ["test", "t"]:
                return self.__test()
            else:
                return self.__development()
        except Exception as error:
            Journal.exception(error)
            return self.data_dict
