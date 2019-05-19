# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/2/13 下午9:17


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    # 定义成绩函数
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


jack = Student('Jack', 80)
jack.print_score()


print(dir(jack))
