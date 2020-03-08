# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/6/20 下午4:02

import time
import sys

file_name = '1.txt'

# 读取1.txt文件
# 在with代码块内，open函数打开文件返回的文件对象通过as重命名为f，通过文件对象f操作文件，操作完文件程序自动关闭文件
try:
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
except FileNotFoundError as msg:
    print('无法打开文件, error is {} ', msg)
except UnicodeDecodeError as msg:
    print('非文本文件无法解析')
    sys.exit()
else:
    for line in lines:
        res = line.rstrip()
        print(res, 'len:', len(res))
        time.sleep(0.5)
finally:
    # f.close()
    print('end it!')


# rstrip()方法去除最后面的字符，默认去除字符串后面的空格
print('make it!66'.rstrip('6'))
