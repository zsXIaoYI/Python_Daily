# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2018/12/17 下午7:24
from functools import reduce

# abs: 求绝对值的函数
a = abs(-1)
print('a:', a)

# abs函数直接赋值给f
f = abs
print(f(-8))


# 一个最简单的高阶级函数,参数f是一个函数
def add(x, y, f):
    return f(x) + f(y)


def f1(x):
    return x * x


def f_reduce(x, y):
    return x + y


def fn(x, y):
    return x * 10 + y


# 将一个字符转换成一个整数
def charToNum(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def strToInt(s):
    def fn1(x, y):
        return x * 10 + y

    def char2Num(s1):
        return DIGITS[s1]

    return reduce(fn1, map(char2Num, s))


def _strToInt(s):
    return reduce(lambda x, y: x * 10 + y, map(charToNum, s))


def _FirstCharToUpperCase(s):
    if len(s) == 0 or s is None:
        raise TypeError('bad str')
    l = len(s)
    if l == 1:
        return s.upper()
    else:
        return s[0:1].upper() + s[1:l]


