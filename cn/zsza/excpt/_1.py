# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2020/3/2 17:41
# @File: _1.py
# __author__ = 'zs'


sep = '-' * 45 + '\n'

print(sep + 'Exception raised and caught')
try:
    x = 'spam'[99]
except IndexError:
    print('except run')
print('1 after run')

print(sep + 'No exception raised')
try:
    x = 'spam'[3]
except IndexError:
    print('except run')
finally:
    print('finally run')
print('2 after run')

# 没有异常会执行else语句
print(sep + 'No exception raised, with else')
try:
    x = 'spam'[3]
except IndexError:
    print('except run')
else:
    print('else run')
finally:
    print('finally run')
print('3 after run')

# except后面的异常不是程序抛出的异常时，finally后面的语句则也不会执行
# 如下面的应该except ZeroDivisionError,而实际上except的IndexError
print(sep + 'Exception raised but not caught')
try:
    x = 1 / 0
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')
