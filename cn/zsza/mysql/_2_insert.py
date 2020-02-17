# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2020/2/17 9:27
# @File: _2_insert.py
# __author__ = 'zs'


import pymysql as pm

db = pm.connect(host='localhost', user='root', password='123456', db='zsql_sy')
cur = db.cursor()

sql = 'insert into _user (u_name) values (\'%s\')'
# noinspection PyBroadException
try:
    cur.execute(sql % '小贼')
    db.commit()
except Exception as e:
    db.rollback()
finally:
    db.close()
