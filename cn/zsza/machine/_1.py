# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/4/9 上午11:23

import numpy as np

X = np.array([[0, 1, 0, 1],
             [1, 1, 1, 0],
             [0, 1, 1, 0],
             [0, 0, 0, 1],
             [0, 1, 1, 0],
             [0, 1, 0, 1],
             [1, 0, 0, 1]])

print(X[True])

y = np.array([0, 1, 1, 0, 1, 0, 0])
print(np.unique(y))  # 返回[0, 1]
counts = {}
for label in np.unique(y):
    # 返回true或false的一个array
    print(y == label)
    # [ True False False  True False  True  True]
    # X[y == label] 则返回下标为True的
    print(X[y == label])
    counts[label] = X[y == label].sum(axis=0)

print('features counts:\n{}'.format(counts))
