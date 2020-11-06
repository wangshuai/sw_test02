# coding=utf-8
# /usr/bin/env python3

'''
Author: swang
Email: 13693554615@163.com

date: 2020-11-03 10:07
'''
import unittest
import requests
from lib.dbconfig import *
from lib.read_excel import *
import json
from config.config import *
from lib.case_log import log_case_info
import os
import sys
sys.path.append('../..')

class TestUserReg(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list(os.path.join(data_path,'test_user_data.xlsx'), 'TestUserReg')

    def test_user_reg_normal(self):
        case_data = get_test_data(self.data_list, 'test_user_reg_normal')
        if not case_data:
            logging.error('用例数据不存在')

        url = case_data.get('url')
        data = json.loads(case_data.get('data'))
        expect_res = json.loads(case_data.get('expect_res'))
        name = data.get('name')

        if check_user(name):
            del_user(name)

        res = requests.post(url=url, json=data)
        log_case_info('test_user_reg_normal', url, data, expect_res, res)
        self.assertDictEqual(res.json(), expect_res)
        self.assertTrue(check_user(name))
        del_user(name)

if __name__ == '__main__':
    unittest.main(verbosity=2)
