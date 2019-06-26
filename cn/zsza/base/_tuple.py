# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2018/11/26 下午9:33

# 另一种有序列表叫元组:tuple，tuple和list非常类似，但tuple一初始化就不能修改

stu = ('Amy', 'Jack', 'Bob')
print('第一个元素:', stu[0])

# 定义一个空的tuple
t = ()
print(t)

# 定义一个只有一个元素的tuple,元素后面要加","
t1 = (1,)
print('定义一个只有一个元素的tuple:', t1)

t2 = ('a', 'b', ['A', 'B'])
t2[2][0] = 'X'
t2[2][1] = 'Y'
print('t2:', t2)

# tuple拆包
name, age = ('小黑', 24)
print('名字:{}, 年龄:{}'.format(name, age))

# divmod函数返回一个tuple,商几余几
print(isinstance(divmod(7, 2), tuple))

# * 运算符把一个可迭代对象拆开作为函数的参数
t = (7, 2)
print(divmod(*t))
