# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2019/12/25 21:47
# @File: _json.py
# __author__ = 'zs'

# python 解析字符串
import json

user_info_dict = {
    "name": "小黑",
    "age": 20,
    "gender": None
}
# 1、转换成json字符串
json_str = json.dumps(user_info_dict, ensure_ascii=False)
print('json_str:', json_str)

# 2、将字符串转换成Python中的dict
py_dict = json.loads(json_str)
print('py_dict:', py_dict)


# 3、dump函数,将Python数据dict写入到json文件
with open('user_info.json', 'w', encoding='utf-8') as f:
    json.dump(user_info_dict, f)


# 4、load函数，加载json文件，并将文件数据转换成Python数据结构
with open('user_info.json', 'r', encoding='utf-8') as f:
    temp_user_info_dict = json.load(f)
    print(temp_user_info_dict)
