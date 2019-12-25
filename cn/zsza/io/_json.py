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
