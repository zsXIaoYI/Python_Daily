# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/4/4 上午11:24

import array

symbols = 'ABD'
codes = []
# ord函数求字符的ascii
for sym in symbols:
    codes.append(ord(sym))
print(codes)

code2 = [ord(sym) for sym in symbols]
print(code2)

# 过滤
code3 = [ord(sym) for sym in symbols if ord(sym) > 65]
print('code3:\n', code3)

code4 = list(filter(lambda c: c > 65, map(ord, symbols)))
print('code4:\n', code4)

# 笛卡尔积
colors = ['black', 'white']
sizes = ['S', 'M', 'L']

t_shirts = [(color, size) for color in colors for size in sizes]
print('t_shirts:', t_shirts)

# 用生成器表达式之后，内存里不会留下一个有6个组合的列表，因为生成器表达式会在
# 每次for循环运行时才产生一个组合
for t_shirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print('t_shirt:', t_shirt)

a = array.array('I', (1, 2, 3))  # I 表示大小为2个字节的无符号整数
print('a:\n', a)

for x in a:
    print(x)

# for循环可以分别提取元组里的元素，也叫作拆包(unpacking)
# 因为元组中第二个元素对我们没有什么用，所以它赋值给"_"占位符
country = [('China', '北京'), ('Japan', '东京'), ('SK', '首尔')]
for cy, _ in country:
    print(cy)

suits = 'spades diamonds clubs hearts'.split()
print(suits)


def seq_search(items: list, elem) -> int:
    """顺序查找"""
    for index, item in enumerate(items):
        if elem == item:
            return index
    return -1


print(seq_search([1, 2, 3, 4], 3))
