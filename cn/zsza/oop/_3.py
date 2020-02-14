# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2020/2/14 21:14
# @File: _3.py
# __author__ = 'zs'

# 最简单的Python类

class rec:
    pass


class rec2:

    def print(self, value):
        print(value)


print(rec.__dict__)
print(list(rec.__dict__))
print(list(rec2.__dict__))

x = rec()
x.name = 'zs'
print(list(x.__dict__))
print(x.__dict__['name'])
