# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2018/11/26 下午5:12

# >>>>>>>>>>>>>>>>Python中的list学习<<<<<<<<<<<<<<<<<<
# list是一个可变的有序列表，类似于Java中的list
# list可用-1位置取最后一个元素

stu = ['Amy', 'Jack', 'Bob']
print('stu:', stu)

l1 = len(stu)
print('list的长度:', l1)

# list中可以按下标进行数组的访问,当索引超出范围时，Python会报一个IndexError
st1 = stu[0]
print('stu中第一个学生:', st1)

st_last = stu[-1]
print('stu中最后一个学生:', st_last)

stu.append('Honey')
print('追加后的stu:', stu)

# 在指定位置插入元素
stu.insert(1, 'David')
print('在指定位置插入元素后:', stu)

# 删除list末尾的元素,并返回该元素
stu_pop = stu.pop()
print('pop:', stu_pop)
print('after pop() stu:', stu)

# pop()可以删除指定位置的元素
p1 = stu.pop(1)
print('删除位置1上的元素:', p1)
print(stu)

print('************************\n')

stu_1 = ['Amy', 'Jack', 'Bob']
stu_1[0] = 'Star'    # 可以替换指定位置上的元素
print('替换后的stu_1:', stu_1)

# list中的元素类型可以不同
L1 = ['Apple', 123, True]
print(L1)

# list中还可以嵌套一个子list
L2 = ['java', ['php', 'C++'], '.Net']
print('L2', L2)
print('L2的长度:', len(L2))  # L2的长度为3

empty_L = []   # 声明一个空的list,其长度为0


# list高级特性:切片
# list[start:end:step],步长默认为1
# list可以进修切片,如果第一个索引为0,还可以省略
L3 = ['Amy', 'Jack', 'Jenny']
print('取L3的前两个元素:', L3[0:2])
print(L3[:2])

print('L3最后两个元素', L3[-2:])

l4 = [1, 2, 3, 4, 5, 6]
print('l4中,从零开始,每隔两个取一个元素:', l4[::2])
print('l4:', l4[:2])

l4.reverse()
print('l4逆序:', l4)
# >>>>>>>>>>>>>>>>>>>>>>>>>列表生成式<<<<<<<<<<<<<<<<<<<<<<<<<<
L4 = [x * x for x in range(1,  6)]
print('L4是否为list类型:', isinstance(L4, list))
print(L4)


g1 = (x * x for x in range(1, 5))
print('g1是否为tuple类型:', isinstance(g1, tuple))
print(g1)

print('------------------------------------\n')
_L = [0, 1, 2, 3, 4, 5, 6, 7]
print('_L的长度:', len(_L))
print('_L[2:5]', _L[2:5])
_L[2:5] = [20, 30, 40]   # 切片的赋值会影响原来list元素
print('after _L:', _L)

bo = ['_'] * 3  # 返回['_', '_', '_']
print(bo)

board = [['_'] * 3 for i in range(3)]
print('board:', board)

_l1 = [3, [66, 55, 44], (7, 8, 9)]
_l2 = list(_l1)
_l1.append(100)  # _l1

print('first _l1:', _l1)
print('first _l2:', _l2)
# 移除55对两者都有影响，两者中的第二个list元素都指向第一个
_l1[1].remove(55)
print('second _l1:', _l1)
print('second _l2:', _l2)

_l2[1] += [33, 22]
print('third _l1:', _l1)
print('third _l2:', _l2)

# 下面操作生成了新的tuple对象，tuple的 += 操作会生成新的tuple
_l2[2] += (10, 11)
print('fourth _l1:', _l1)
print('fourth _l2:', _l2)

# 字符串转换为List
print(list('abc'))
