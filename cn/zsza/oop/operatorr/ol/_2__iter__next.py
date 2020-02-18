# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2020/2/18 18:33
# @File: _2__iter__next.py
# __author__ = 'zs'


class Squares:

    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2


for i in Squares(1, 3):
    print(i, end=' ')
X = Squares(1, 3)
print('\n*****************')

Sq = iter(X)
print(next(Sq))
