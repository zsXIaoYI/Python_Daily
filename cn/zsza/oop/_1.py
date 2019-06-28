# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/5/19 下午3:04


class Student(object):
    # 注意init的拼写，否则报错: TypeError: Student() takes no arguments
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s,正在学习%s' % (self.name, course_name))

    def is_adult(self):
        if self.age < 18:
            print('未成年')
        else:
            print('成年人')


def main():
    stu1 = Student('小黑', 20)
    stu1.study('Python语言设计')
    stu1.is_adult()


if __name__ == '__main__':
    main()
    print('hello', 'world', sep=',', end='!')
