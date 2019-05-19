# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/2/15 下午8:57


class Student(object):
    # 两个下划线开头的变量是私有的
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
