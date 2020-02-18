# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2020/2/18 17:06
# @File: _1_getitem.py
# __author__ = 'zs'


class Number:
    def __init__(self, start):
        self.data = start

    def __sub__(self, other):
        return Number(self.data - other)


X = Number(5)
Y = X - 2
print(Y.data)


class Indexer:
    def __getitem__(self, index):
        return index ** 2


indx = Indexer()
print(indx[2])  # calls indx.__getitem__(2)


# 切片操作
class IndexSlice:
    data = [5, 6, 7, 8, 9]

    def __getitem__(self, index):
        print('getitem:', index)
        return self.data[index]


idxSlice = IndexSlice()
print('第一个元素:', idxSlice[0])
print('从第一个元素到最后一个元素:', idxSlice[1:])
print('每隔1个取一个元素:', idxSlice[::2])


class StepperIndex:
    def __getitem__(self, i):
        return self.data[i]


stp = StepperIndex()
stp.data = 'Spam'
for item in stp:
    print(item, end=' ')
