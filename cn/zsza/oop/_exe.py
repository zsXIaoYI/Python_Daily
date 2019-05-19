# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/3/24 下午4:46


class test:
    def __init__(self, val=None):
        self.val = val

    def print(self):
        return self.val


t = test('Mon')
print(t.print())
