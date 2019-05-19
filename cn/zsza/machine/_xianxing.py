# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/3/31 下午11:06

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq


X = np.array([8.19, 2.72, 6.39, 8.71, 4.7, 2.66, 3.78])
Y = np.array([7.01, 2.78, 6.47, 6.71, 4.1, 4.23, 4.05])


def func(p, x):
    k, b = p
    return k * x + b


def error(p, x, y, s):
    print('s:', s)
    return func(p, x) - y


p0 = [1, 1]
paras = leastsq(error, p0, args=(X, Y, ''))
print(paras[0])
print(isinstance(paras[0], np.ndarray))

k, b = paras[0]  # k斜率， b偏执
print(k, b)

plt.figure(figsize=(8, 6))
plt.scatter(X, Y, color='red', label='Sample Point', linewidth=3)

x = np.linspace(0, 10, 1000)  # 0到10取1000个点
y = k * x + b

plt.plot(x, y, color='orange', label='Fitting Line', linewidth=2)
plt.show()
