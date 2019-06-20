# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/6/20 下午4:02

import time
import sys

file_name = '1.txt'

# 读取1.txt文件
try:
    with open(file_name) as f:
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
    print('end it!')


# rstrip()方法去除最后面的字符，默认去除字符串后面额空格
print('make it!66'.rstrip('6'))
