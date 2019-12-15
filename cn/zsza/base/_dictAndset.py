# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2018/11/28 下午9:26

# Python内置了dict, 和Java中的Map类似，如果查找的key不存在，则报KeyError
# set类似于Java中的HashSet
# 多次对一个key放入value,会覆盖之前的value
# 正确使用dict非常重要,需要牢记的第一条就是dict的key必须是不可变对象
# 在Python中，字符串、整数都是不可变的
d = {'Jack': 18, 'Amy': 23}
# 用如下方式得到key所对应的value，如果key不存在的话，则报KeyError
print('Jack年龄:', d['Jack'])
print('Amy年龄:', d.get('Amy'))
print('d的长度:', len(d))

# 如下类似于java中的Map的put操作
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

# pop删除dict中的一个键值对，并返回value
v = d.pop('Jack')
print('pop的值:', v)
print('after pop:', d)

d1 = {'city': '北京', 'area': 200}
print(d1.get('city'))
print(d1.get('area'))

print('**************dict迭代*************')
# 迭代key
for key in d1.keys():
    print('key:', key)
# 迭代键值对
for key, value in d1.items():
    print('{} : {}'.format(key, value))

# item是tuple类型
for item in d1.items():
    print(item)

print('>>>>>>>>>>>>>>>>>> set集合 <<<<<<<<<<<<<<<<<<<\n')
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

# list作为一个参数传入update方法，合并成一个新的set
s1.update([3, 5])
print('after update:', s1)

# Python中dict的key不支持list或dict类型，因为list和dict类型是unhashable的
# 因为Python的list和dict都是可变对象，可以动态地添加或删除元素,以下两行代码会报unhashable typpe: 'list'
# _s2 = set([(1, 2, [1, 2]), (2, 3, [6, 8])])
# print('_s2:', _s2)

_s1 = set([(1, 2, 3), (2, 3, 4)])
print('_s1:', _s1)

dd = {'one': "This is one", 2: "This is two"}
print(dd)

DIAL_CODES = [(86, 'China'), (91, 'India'), (36, 'Brazil')]
country_code = {country: code for code, country in DIAL_CODES}
print('country_code:', country_code)

new_country_code = {code: country.upper() for country, code in country_code.items() if code > 50}
print('new_country_code:', new_country_code)
