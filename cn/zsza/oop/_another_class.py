# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/5/24 下午8:47


# 类的另一种创建形式
def bar(self, name):
    self._name = name


def foo(self, course_name):
    print('%s正在学习%s.' % (self._name, course_name))


def main():
    student = type('Student', (object,), dict(__init__=bar, study=foo))
    stu1 = student('Amy')
    stu1.study('Python程序设计')


if __name__ == '__main__':
    main()
