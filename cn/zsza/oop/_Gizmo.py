# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/4/9 下午11:04


class Gizmo(object):
    # 注意init的拼写
    def __init__(self):
        print('Gizmo id: %d' % id(self))


x = Gizmo()
print(x)


