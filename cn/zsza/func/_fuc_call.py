# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2018/12/17 下午7:29
from functools import reduce
from typing import Iterable, Iterator

import Func_1

a = Func_1.add(1, 3, abs)
print('a:', a)

# >>>>>>>>>>>>>>>>>>>>map/reduce<<<<<<<<<<<<<<<<<<<<

# m返回一个map对象
m = map(Func_1.f1, [1, 2, 3])
print(m)
print(isinstance(m, Iterable))  # m支持迭代
print('m转换成list:', list(m))

# 把list中的整型元素转换成字符串
m1 = map(str, [1, 2, 3, 4])
print(list(m1))

# reduce的示例解释
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
a1 = reduce(Func_1.f_reduce, [1, 3, 5])
print('a1:', a1)

# 将list中的整型元素转换成一个大的阿拉伯数字
a2 = reduce(Func_1.fn, [1, 3, 5, 7, 9])
print('a2:', a2)

a3 = reduce(Func_1.fn, map(Func_1.charToNum, '13579'))
print('a3:', a3)

a4 = Func_1.strToInt('5621')
print('a4:', a4)

print(Func_1._FirstCharToUpperCase('abc'))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def sort_byName(t):
    return t[0]


L1 = sorted(L, key=sort_byName)
print('按名字排序后:', L1)
