# coding=utf-8
# /usr/bin/env python3

'''
Author: swang
Email: 13693554615@163.com

date: 2020-11-03 10:06
'''
import logging
import os

prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_path = os.path.join(prj_path, 'data')
test_path = os.path.join(prj_path, 'test')

log_file = os.path.join(prj_path, 'log', 'log.txt')
report_file = os.path.join(prj_path, 'report', 'report.html')

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=log_file,
                    filemode='a')
db_host = '127.0.0.1'
db_port = 3306
db_user = 'root'
db_passwd = 'asdf1234'
db = 'sw_test'

smtp_server = 'smtp.163.com'
smtp_user = '13693554615@163.com'
smtp_password = 'DWSBWWENHZPEUZKB'

sender = smtp_user
receiver = '793138041@qq.com'
subject = '接口测试报告'

if __name__ == '__main__':
    logging.info('hello')