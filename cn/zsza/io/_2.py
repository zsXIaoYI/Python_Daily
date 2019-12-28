# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/6/20 下午4:54


import time


def main():
    # 一次性读取整个文件的内容
    with open('1.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    print('.........')
    # 逐行读取文件
    with open('1.txt',  encoding='utf-8') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print('\n***********')

    # 读取到一个list中
    with open('1.txt', encoding='utf-8') as f:
        lines = f.readlines()
        print('lines:', lines)


if __name__ == '__main__':
    main()
