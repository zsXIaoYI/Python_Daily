# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/6/17 下午7:42

import csv

# 1、读取csv文件
file_name = 'example.csv'

try:
    with open(file_name) as f:
        reader = csv.reader(f)
        data = list(reader)
except FileNotFoundError:
    print('无法打开文件:', file_name)
else:
    for item in data:
        print((item[0], item[1], item[2]))


# 2、写入csv文件
class Teacher(object):

    def __init__(self, name, age, title):
        self.__name = name
        self.__age = age
        self.__title = title
        self.__index = -1

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def title(self):
        return self.__title


teacher_file_name = 'teacher.csv'
teachers = [Teacher('小黑', 24, '小黑真黑'), Teacher('小白', 29, ' 小白也黑')]

try:
    with open(teacher_file_name, 'w') as f:
        writer = csv.writer(f)
        for teacher in teachers:
            writer.writerow([teacher.name, teacher.age, teacher.title])
except BaseException as e:
    print('无法写入文件:', e)
else:
    print('保存数据完成!')
