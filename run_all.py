# coding=utf-8
# /usr/bin/env python3

'''
Author: swang
Email: 13693554615@163.com

date: 2020-11-05 14:57
'''
import HTMLTestRunner
import unittest
from config.config import *
from lib.send_email import send_email

logging.info("====================== 测试开始 ======================")
suite = unittest.defaultTestLoader.discover(test_path)

# 三方库HTMLTestRunner报告
with open(report_file, 'wb') as f:
    HTMLTestRunner.HTMLTestRunner(stream=f, title='sw_测试报告').run(suite)

send_email(report_file)
logging.info("====================== 测试结束 ======================")
