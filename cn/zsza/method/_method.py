# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2018/12/4 下午2:20

import math


# 定义一个空函数
def nop():
    pass


# 求一个整数的绝对值
def my_abs(x):
    if not isinstance(x, int):
        raise TypeError('不是整数')
    if x >= 0:
        return x
    else:
        return -x


def my_abs_(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x > 0:
        return x
    else:
        return -x


# Python函数返回多个值，angle为默认参数
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


# 求解一元二次方程
def quadratic(a, b, c):
    sq_b = b * b
    temp = 4 * a * c
    if sq_b < temp:
        return '无解'
    elif sq_b == temp:
        s1 = -b / 2 * a
        s2 = s1
        return s1, s2
    else:
        s1 = (-b + math.sqrt(sq_b - temp)) / (2 * a)
        s2 = (-b - math.sqrt(sq_b - temp)) / (2 * a)
        return s1, s2


# 对于power函数而言，参数x是一个位置参数
def power(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad type Error')
    return x * x


# 求x的n次幂，x和n也称作位置参数
# n声明为2，则称为默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s = s * x
    return s


# city默认为Beijing
def enroll(name, gender, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('city:', city)


# L指向一个可变List
def add_end(L=[]):
    L.append('end')
    return L


# L指向一个不可变对象None
def add_end_2(L=None):
    if L is None:
        L = []
    L.append('end')
    return L


# 求一系列数的平方和
# 调用的时候，需要先组装出一个list或tuple
def calc(numbers):
    add = 0
    for i in numbers:
        add = add + i * i
    return add


# 带有可变参数的函数
# *numbers为可变参数,number是个tuple类型
def calc_2(*numbers):
    print('*numbers:', *numbers)
    print('*numbers是否为tuple类型:', isinstance(numbers, tuple))
    add = 0
    for n in numbers:
        add = add + n * n
    return add


# 带有关键字参数的函数
# kw是个dict类型
def print_per(name, age, **kw):
    # print(isinstance(kw, dict))
    print('name:', name, 'age:', age, 'other:', kw)


# 带有命名关键字参数的函数
# 后面必须跟city和job参数
def _print_per(name, age, *, city, job):
    print(name, age, city, job)


# 带有可变参数，命名关键字的函数
# *args的参数后面为命名关键字的参数，args是个tuple类型
def print_per_1(name, age, *args, city, job):
    # print(isinstance(args, tuple))
    print(name, age, args, city, job)


def print_per_2(name, age, *, city='堪培拉', job):
    print(name, age, city, job)


def product(x, *args):
    res = x
    for n in args:
        res = res * n
    return res


# 实现去除首位空格
def str_trim(s):
    le = len(s)
    begin = 0
    end = le - 1
    if le == 0:
        return 'empty str'
    elif begin == end:
        return 'length is 1'
    else:
        while begin < end:
            if s[begin:begin + 1] == ' ':
                begin += 1
            elif s[end:end + 1] == ' ':
                end -= 1
            else:
                print('end....')
                break
        return s[begin:end + 1]


def findMaxAndMin(L):
    if not isinstance(L, list):
        raise TypeError('error type')
    elif len(L) == 0:
        raise ValueError('empty list')
    elif L is None:
        raise TypeError('list is None')
    ma = L[0]
    mi = L[0]
    for li in L:
        if li > ma:
            ma = li
        elif li < mi:
            mi = li
    return mi, ma
