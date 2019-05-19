# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/3/10 下午12:21


import pandas as pd


x1 = pd.ExcelFile('/file/test.xlsx')
print('sheet_names: {0}'.format(x1.sheet_names))
