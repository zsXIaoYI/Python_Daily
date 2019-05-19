# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2018/12/4 下午2:20


print(len(''))

print('abc'[0:1])
print('abc'[1:2])
print('abc'[2:3])

l1 = [1, 2, 3]
print(l1[:])  # 返回[1, 2, 3]
print(l1[::])  # 返回[1, 2, 3]
print(l1[:-1])  # 返回[1, 2]

print(l1[::-1])  # 列表反转，返回[3, 2, 1]


def factorial(n):
    """return n!"""
    return 1 if n < 2 else n * factorial(n - 1)


l2 = list(map(factorial, range(6)))
print(l2)


print(factorial(5))
print(factorial.__doc__)
print(type(factorial))
