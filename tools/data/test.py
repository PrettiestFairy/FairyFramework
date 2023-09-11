# coding: utf8
""" 
@ File: test.py
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

import os
import pandas as pd
import numpy as np

from modules.journals import JournalsModule
from utils.publics import PublicUtilsStaticClass


class TestStaticClass:
    """
    测试静态类
    """

    def __init__(self):
        pass

    @staticmethod
    @JournalsModule.catch()
    def merge_csv_row(file_a, file_b, merge_csv_path=None) -> str:
        """
        垂直拼接, 沿着列的方向, 对行进行拼接
        :param file_a: 文件1
        :param file_b: 文件2
        :param merge_csv_path: 合并后的文件路径或者文件名
        :return: 合并后的文件路径
        """
        try:
            if merge_csv_path is None:
                merge_csv_path = 'new_merge_data.csv'
            else:
                merge_file_path, merge_file_name = os.path.split(merge_csv_path)
                merge_file_path = PublicUtilsStaticClass.path_root_conver_system_separator(os.path.join(PublicUtilsStaticClass.path_root, merge_file_path))
                if os.path.isdir(merge_file_path) is False:
                    os.mkdir(merge_file_path)
            JournalsModule.info('文件位置: {}'.format(file_a))
            JournalsModule.info('文件位置: {}'.format(file_b))
            data_a_array = np.array(pd.read_csv(file_a))
            data_b_array = np.array(pd.read_csv(file_b))
            merge_array = np.row_stack((data_a_array, data_b_array))
            merge_retuls = pd.DataFrame(merge_array)
            merge_file_path = PublicUtilsStaticClass.path_root_conver_system_separator(os.path.join(PublicUtilsStaticClass.path_root, merge_csv_path))
            merge_retuls.to_csv(merge_file_path, index=False, header=False)
            JournalsModule.info('保存位置: {}'.format(merge_file_path))

            return merge_file_path
        except Exception as error:
            JournalsModule.exception(error)
