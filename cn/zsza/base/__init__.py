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


colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts = [(color, size) for color in colors for size in sizes]
print('tshirts:', tshirts)

a = array.array('I', (1, 2, 3))  # I 表示大小为2个字节的无符号整数
print('a:\n', a)

for x in a:
    print(x)

# divmod函数返回一个tuple,商几余几
print(isinstance(divmod(7, 2), tuple))

# * 运算符把一个可迭代对象拆开作为函数的参数
t = (7, 2)
print(divmod(*t))

# for循环可以分别提取元组里的元素，也叫作拆包(unpacking)
# 因为元组中第二个元素对我们没有什么用，所以它赋值给"_"占位符
country = [('China', '北京'), ('Japan', '东京'), ('SK', '首尔')]
for cy, _ in country:
    print(cy)


