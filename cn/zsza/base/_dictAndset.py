# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2018/11/28 下午9:26

# Python内置了dict, 和Java中的Map类似，如果查找的key不存在，则报KeyError
# set类似于Java中的HashSet
# 多次对一个key放入value,会覆盖之前的value
# 正确使用dict非常重要,需要牢记的第一条就是dict的key必须是不可变对象
# 在Python中，字符串、整数都是不可变的
d = {'Jack': 18, 'Amy': 23}
print('Jack年龄:', d['Jack'])
print('Amy年龄:', d.get('Amy'))
print('d的长度:', len(d))

d['May'] = 25
print('新的dict:', d)
print('May的年龄:', d['May'])

# 如果key存在，则返回该key对应的值；如果key不存在，则返回设定的value
print(d.get('May', 28))

# 判断key是否存在有两种方法
# 1、用in关键字
is_exist = 'David' in d
print('is_exist:', is_exist)

# 2、用get方法，不存在则返回None
res = d.get('Jenny')
print('Jenny是否存在:', res)
print(res is None)

v = d.pop('Jack')
print('pop的值:', v)
print('after pop:', d)

d1 = {'city': '北京', 'area': 200}
print(d1.get('city'))
print(d1.get('area'))

# >>>>>>>>>>>>>>>>>> set <<<<<<<<<<<<<<<<<<<
# set集合元素不能重复,要创建一个set，需要提供一个list作为输入集合
# 1、可以用add()方法添加元素
# 2、可以用remove()方法删除元素
s = set([1, 2, 4])
print('s:', s)

s.add(3)
print('after add s:', s)

s.remove(4)
print('after remove s:', s)

# set集合可以做交集和并集
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print('s1于s2的交集:', s1 & s2)
print('s1与s2的并集:', s1 | s2)

# Python中dict的key不支持list或dict类型，因为list和dict类型是unhashable的
# 因为Python的list和dict都是可变对象，可以动态地添加或删除元素
# s2 = set([(1, 2, [1, 2]), (2, 3, [6, 8])])
print(s2)

s1 = set([(1, 2, 3), (2, 3, 4)])
print(s1)

dd = {'one': "This is one", 2: "This is two"}
print(dd)
