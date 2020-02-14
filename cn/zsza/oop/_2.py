# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2020/2/14 20:40
# @File: _2.py
# __author__ = 'zs'


class FirstClass:
    def setData(self, value):
        self.data = value

    def display(self):
        print('First Class data:', self.data)


class SecondClass(FirstClass):
    def display(self):
        print('Current value = "%s"' % self.data)


class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value

    # 当对象出现+表达式时，该方法会被调用
    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):
        return '[ThirdClass: %s]' % self.data

    def mul(self, other):
        self.data *= other


a = ThirdClass('abc')
a.display()
print(a)

# a和字符串的位置不能颠倒
b = a + 'zs'
b.display()
print(b)

a.mul(3)
print('after mul operate, a:', a)

