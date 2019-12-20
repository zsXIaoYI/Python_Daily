# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2019/12/20 21:59
# @File: _senior_method.py
# __author__ = 'zs'


# 普通求和函数
def sum(x, y):
    return x + y


# 闭包,求两个数字的和
def sum_closure(x):
    # 内部函数
    def sum_inner(y):
        return x + y

    # 外部函数 返回值是内部函数的引用
    return sum_inner


rs1 = sum(10, 1)
print('rs1:', rs1)

# rs_func是个function类型
rs_func = sum_closure(10)
print('rs_func:', rs_func)

rs2 = rs_func(2)
print('rs2:', rs2)


# 定义一个计数器,声明base和step两个默认参数，base:初始值，step:步长
def counter_func(base=0, step=1):
    print('base:{}, step:{}'.format(base, step))
    return base + step


c1 = counter_func()
print('当前计数器的值:', c1)

# 有两个默认参数的函数，传递一个参数进去，先给第一个参数赋值，第二个还是默认
c2 = counter_func(c1)
print('当前计数器的值:', c2)

print('\n')


def counter_closure(base=0):
    # 在外部定义一个列表类型的变量
    cnt_base = [base]
    print('cnt_base类型', isinstance(cnt_base, list))

    def counter(step=1):
        cnt_base[0] += step
        # print('counter中的cnt_base:', cnt_base)
        return cnt_base[0]
    return counter


counter = counter_closure()
print('当前计数器为:', counter())
print('当前计数器为:', counter())
