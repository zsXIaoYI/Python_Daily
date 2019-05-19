# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/3/10 下午2:56


import numpy as np

x = np.array([[1, 3, 4], [4, 5, 6], [7, 8, 9]])
print('x=', x)

print(x.shape)  # 返回几行几列
print(x.size)   # 返回矩阵元素的个数
print(x.dtype)  # 返回int64

x1 = np.zeros((3, 4))  # 创建一个元素全为0的三行四列的矩阵

x2 = np.arange(4)
print('x2:', x2)

x3 = np.arange(10) ** 3
print('x3:', x3)
print('x3[2:5]=', x3[2:5])

arr = np.ones((3, 4))
print(arr)

a = np.array([20, 30, 40, 50])
print(a)
print(a.shape)


def fn(n):
    a = np.arange(n * n).reshape((n, n))
    a[(n - 1), :] = n  # n-1行所有列都为n
    return a


print(fn(4))
