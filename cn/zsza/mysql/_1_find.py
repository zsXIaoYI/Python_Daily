# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2020/2/16 11:52
# @File: _1_find.py
# __author__ = 'zs'

import pymysql as pm

db = pm.connect(host='localhost', user='root', password='123456', db='zsql_sy')

cur = db.cursor()

sql = 'select * from _user'
try:
    cur.execute(sql)
    result = cur.fetchall()
    print(result)
    print('遍历查询的数据:')
    for row in result:
        id = row[0]
        name = row[1]
        print('id: {}, name : {}'.format(id, name))
except Exception as e:
    raise e
finally:
    print('finally....')
    db.close()
