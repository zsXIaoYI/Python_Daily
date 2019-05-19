# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/4/9 下午11:04


class Gizmo(object):

    def __int__(self):
        print('Gizmo id: %d' % id(self))


x = Gizmo()
print(x)

t1 = (1, 2, [20, 30])
print(t1[-1])