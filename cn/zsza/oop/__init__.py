# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/2/13 下午9:16

import types
from _Animal import Animal


def fn():
    pass


print(type(123))

print(types.FunctionType)
print(type(fn))

print('\n'.join([''.join([('Love '[(x - y) % len('Love ')] if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (
        x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))

print(Animal)
an = Animal()
an.run()