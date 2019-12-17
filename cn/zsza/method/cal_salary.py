# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2019/12/17 21:48
# @File: cal_salary.py
# __author__ = 'zs'


# 计算医疗和养老保险缴纳的钱数
def insurance(basic, **kvargs):
    # 医疗保险
    health = kvargs.get('health')
    # 养老保险
    pension = kvargs.get('pension')

    cost = basic * health + basic * pension
    return cost


# 计算个税
def tax(balance):
    if balance <= 5000:
        return 0
    elif 5000 < balance <= 10000:
        return balance * 0.05
    elif 10000 < balance <= 30000:
        return balance * 0.1
    else:
        return balance * 0.2


# 计算实发工资
def pay(basic):
    cost_dict = {'health': 0.02, 'pension':0.08}
    # 计算社保
    cost = insurance(basic, **cost_dict)
    balance = basic - cost

    tax_fee = tax(balance)
    pay_fee = balance - tax_fee
    print('基本工资: {}, 社保缴费: {}, 个税: {}, 实发工资: {}'.format(basic, cost, tax_fee, pay_fee))


pay(8000)
