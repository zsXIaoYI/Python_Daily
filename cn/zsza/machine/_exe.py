# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/3/16 下午5:19


import pandas as pd
import numpy as np

x1 = pd.ExcelFile('/PyCharm_Space/PythonDaily/file/1.2.test.xlsx')
df = x1.parse('basic_info')

print(df)

avg = df.mean(0)
print('平均score:', avg['score'])

for index, row in df.iterrows():
    tp = row['type']
    name = row['name']
    score = row['score']
    print(tp, '\t', name, '\t', score)


df = df.fillna(avg['score'])
print('after fillna \n:', df)

pd.DataFrame(df).to_excel('new.xlsx', sheet_name='basic')
