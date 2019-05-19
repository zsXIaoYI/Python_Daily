# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2018/12/4 下午5:05

'aaa'

import _method
import math

# from _method import *

print(_method.my_abs(-27))

x, y = _method.move(100, 100, 60, math.pi / 6)
print(x, y)

r = _method.move(100, 100, 60, math.pi / 6)
print(r)
print('r是否是个tuple类型:', isinstance(r, tuple))

print(isinstance(_method.quadratic(1, -6, 9), tuple))
print(_method.quadratic(1, -6, 9))
print(_method.quadratic(1, -5, 6))

print(_method.power(3, 4))

# 调用_method.power(5) 会报错
# TypeError: power() missing 1 required positional argument: 'n'
# print(_method.power(5))

# power(x, n)中默认声明n为2，则下面power(5)调用,实则调的是power(5, 2)
print(_method.power(5))

_method.enroll('xx', 'male')
_method.enroll('yy', 'female', city='tianjin')

# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
# 如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了
# 定义默认参数要牢记一点：默认参数必须指向不变对象
print(_method.add_end())
print(_method.add_end())  # 返回['end', 'end']

print(_method._add_end())
print(_method._add_end())

print('1, 3, 5的平方和为:', _method.calc([1, 3, 5]))

# 传入的1, 2, 3为可变参数
print('1, 2, 3的平方和为:', _method._calc(1, 2, 3))

# *nums表示把nums这个list的所有元素作为可变参数传进去
nums = [1, 2, 3]
print('list转换成可变参数求元素的平方和:', _method._calc(*nums))

_method.print_per('xiaoan', 18, city='beijing')
_method.print_per('xiaoan', 19, gender='male', city='beijing')

extra = {'city': 'bj', 'job': 'engineer'}
_method.print_per('Jack', 24, city=extra.get('city'), job=extra['job'])
# 上面调用可以这么写
_method.print_per('Amy', '20', **extra)

print('带有命名关键字参数调用')
_method._print_per('小白', 25, city='nanjing', job='php programming')

_method.print_per_1('小鱼', 23, 'hobby', 'game', city='shanghai', job='写php的')

_method.print_per_2('小熊', 26, job='写Python')

print(_method.product(3, 5, 6))

print(len(_method.str_trim('  a bc')))

print(_method.findMaxAndMin([1, -2, 3, 8, 7]))


ss = set(['aa', 'vdd'])
aa = 'aa'

print(aa in ss)
