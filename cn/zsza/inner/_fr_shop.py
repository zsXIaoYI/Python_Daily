# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/4/4 上午11:24

# 列表生成器


class Fruit(object):

    def __getitem__(self, item):
        return self.fruits[item]


if __name__ == '__main__':
    fr = Fruit()
    print(fr)

    fr.fruits = ['apple', 'banana', 'pear']
    for item in fr:
        print(item)

print(ord('A'))
