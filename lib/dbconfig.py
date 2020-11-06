# coding=utf-8
# /usr/bin/env python3

'''
Author: swang
Email: 13693554615@163.com

date: 2020-11-03 10:06
'''
import pymysql
from config.config import *
import sys
sys.path.append('..')

def get_db_conn():
    conn = pymysql.connect(host=db_host,
                           port=db_port,
                           user=db_user,
                           password=db_passwd,
                           db=db,
                           charset='utf8')
    return conn

def query_db(sql):
    conn = get_db_conn()
    cur = conn.cursor()
    logging.debug(sql)
    cur.execute(sql)
    result = cur.fetchall()
    logging.debug(result)
    cur.close()
    conn.close()
    return result

def change_db(sql):
    conn = get_db_conn()
    cur = conn.cursor()
    logging.debug(sql)
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
        logging.error(str(e))
    finally:
        cur.close()
        conn.close()

def check_user(name):
    sql = "select * from users where name = '{}'".format(name)
    result = query_db(sql)
    return True if result else False

def add_user(name, password):
    sql = "insert into users (name, password) value ('{}','{}')".format(name, password)
    change_db(sql)

def del_user(name):
    sql = "delete from users where name = '{}'".format(name)
    change_db(sql)