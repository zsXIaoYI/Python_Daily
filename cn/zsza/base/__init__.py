# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/4/4 上午11:24

import array



a = array.array('I', (1, 2, 3))  # I 表示大小为2个字节的无符号整数
print('a:\n', a)

for x in a:
    print(x)





def seq_search(items: list, elem) -> int:
    """顺序查找"""
    for index, item in enumerate(items):
        if elem == item:
            return index
    return -1


print(seq_search([1, 2, 3, 4], 3))
