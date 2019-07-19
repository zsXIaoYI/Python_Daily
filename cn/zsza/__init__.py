# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2018/12/4 下午2:09


import re


def main():
    user_name = input('请输入用户名:\n')
    qq = input('请输入qq号:\n')
    # 用户名必须由字母、数字或下划线构成且长度在6~20个字符之间
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', user_name)
    if not m1:
        print('请输入有效的用户名.')
    # QQ号是5~12的数字且首位不能为0
    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m2:
        print('请输入有效的QQ号.')
    if m1 and m2:
        print('你输入的信息是有效的!')


if __name__ == '__main__':
    main()
