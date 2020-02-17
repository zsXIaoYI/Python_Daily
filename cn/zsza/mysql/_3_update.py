# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2020/2/17 9:38
# @File: _3_update.py
# __author__ = 'zs'


import pymysql as pm

db = pm.connect(host='localhost', user='root', password='123456', db='zsql_sy')
cur = db.cursor()

sql = "update _user set u_name = '%s' where id = %d"
# 删除操作
sql_del = "delete from _user where id = %d"

# noinspection PyBroadException
try:
    cur.execute(sql % ('小法', 3))
    db.commit()
except Exception as e:
    db.rollback()
finally:
    db.close()
