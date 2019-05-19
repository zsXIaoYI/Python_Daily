# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/2/19 下午5:55


import pymysql


db = pymysql.connect('10.12.0.29', 'root', 'moIf2tZzvrDt', 'mryt_cps_122510')
cr = db.cursor()

sql = 'select * from t_vip_base_info limit 2'

cr.execute(sql)


data = cr.fetchall()

print('data类型:', isinstance(data, tuple))
print(len(data))

print(data)

cr.close()
db.close()
