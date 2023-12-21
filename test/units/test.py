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

from tools.publics import PublicToolsBaseClass
from modules.journals import InitJournalModulesClass
from modules.configuration import InitConfigClass
from modules.decorator import TimingDecorator
from tools.publics import InitDateTimeClass

import gmpy2
import hashlib


class TestClass(PublicToolsBaseClass):
    def __init__(self):
        PublicToolsBaseClass.__init__(self)

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
                InitDateTimeClass.datetimes.timestamp_dt("2023-01-01 00:00:01"),
                InitDateTimeClass.datetimes.datetime_ts(1701018899),
            )
        )

    def test4(self):
        try:
            p = 8666789885346075954582743436174521581697
            q = 2449181960789395782044494299423558347143
            result = pow(
                8232151627233115772131180151146951323147507324398914513031444555762539986162650,
                gmpy2.invert(37777, (p - 1) * (q - 1)),
                (p * q),
            )
        except Exception as error:
            result = error

        return result

    def test6(self, data):
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.backends import default_backend
        from cryptography.hazmat.primitives.asymmetric import rsa, padding
        from cryptography.hazmat.primitives import serialization

        # 生成 RSA 密钥对
        private_key = rsa.generate_private_key(
            public_exponent=65537, key_size=2048, backend=default_backend()
        )

        public_key = private_key.public_key()

        # 将字符串转换为字节
        data = data.encode()

        # 使用公钥进行加密
        encrypted_data = public_key.encrypt(
            data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )

        print("加密后的数据:", encrypted_data)

        # 将公钥保存到文件（可选）
        with open("public_key.pem", "wb") as public_key_file:
            public_key_file.write(
                public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo,
                )
            )

        # 将私钥保存到文件（请保持安全）
        with open("private_key.pem", "wb") as private_key_file:
            private_key_file.write(
                private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.NoEncryption(),
                )
            )

    def test7(self):
        pwd = hashlib.sha1("5cO@^@w\K<O4m6Tz58".encode("utf8"))
        print(pwd.hexdigest())
        from Crypto.Hash import SHA1

        sha1 = SHA1.new()
        sha1.update("5cO@^@w\K<O4m6Tz58".encode("utf8"))
        pwd_2 = sha1.hexdigest()
        print(pwd_2, type(pwd_2))
        print(
            len(
                "b2e14e1f3778dfcb0d92cba02c6efd211e654762d0389337d0a95d76ce18b9b32d7f3b00"
                "f02b3bb39d85dcf0c900693709c96e580cb5b482eeff604ee44dc1e1c6c4bc42c4a6f9dd6e5f0971da8885d6379b4e18"
            )
        )
        


class TestClass02:
    """Test"""

    def __str__(self):
        results = "Str - TestClass2"
        return results

    def t_1(self):
        results = True
        return results
    
    @staticmethod
    def t_2():
        tc = TestClass()
        s1 = tc.api_results()
        s2 = tc.root_path
        print(s1, s2)


def main(*args, **kwargs):
    print(TestClass02.t_2())
    return True


if __name__ == "__main__":
    print(main())
