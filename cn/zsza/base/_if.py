# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2018/11/26 下午9:49

age = 4
if age >= 18:
    print('your age is', age)
    print('adult')
elif 5 <= age < 18:
    print('your age is', age)
    print('teenager')
else:
    print('your age is', age)
    print('kid')

# 只要x是非零数值、非空字符、非空list，就判断为True
x = 1
if x:
    print(True)

