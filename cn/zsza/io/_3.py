# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/6/20 下午5:34

from math import sqrt

print(sqrt(2))  # 开方

# a为追加
with open('prime.txt', 'a') as f:
    for num in range(2, 10):
        f.write(str(num) + '\n')
print('写入完成')


class test(object):
    # val为默认参数
    def __init__(self, val=None):
        self.val = val

    def print(self):
        return self.val


t = test('Mon')
print(t.print())
