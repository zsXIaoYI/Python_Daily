# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/7/30 上午10:45

# start默认为0，step默认为1
l1 = list(range(5))
print('l1:', l1)

# 指定初始值为1,步长为2
l2 = list(range(1, 10, 2))
print('l2:', l2)

# 步长为负数时，start比end大
l3 = list(range(9, 0, -2))
print('l3:', l3)

l4 = [1, 2, 3, 4, 5, 6]
print('l4:', l4[::2])
print('l4:', l4[:2])

l4[::2] = range(3)
print('after slice l4:', l4)

# range支持序列拆包赋值
x, y, z = range(3)
print(x, y, z)


print(list(range(1, 5)))
