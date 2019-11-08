# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = 'zs'

# 使用__slots__
class Student(object):
    pass


def set_age(self, age):
    self.age = age


from types import MethodType

stu = Student()
stu.set_age = MethodType(set_age, stu)  # 给实例绑定一个方法
stu.set_age(18)
print('绑定set_age方法后：', stu.age)

stu1 = Student()


# stu1.set_age(23)               # 这样对stu1不起作用

# 为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self, score):
    self.score = score


Student.set_score = MethodType(set_score, Student)
stu2 = Student()
stu2.set_score(88)
print('给你class绑定set_score方法后：', stu2.score)


# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
class Person(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


per = Person()
per.age = 18
print('per的age=', per.age)  # 绑定per.score会报错


class PP(Person):
    pass


pp = PP()
pp.name = '李三'
print(pp.name)


# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：

class xueSheng(object):
    def get_score(self):
        return self.__score

    def set_score(self, score):
        value = score
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')


xs = xueSheng()
xs.set_score(89)
print(xs.get_score())


# xs.set_score(120)     # 120不在0~100之间,会报错
class xueSheng2(object):

    def __init__(self):
        self._score = None

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        # value = score
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


xs2 = xueSheng2()
xs2.score = 88
print('学生2的成绩:', xs2.score)


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


sc = Screen()
sc._width = 18
sc._height = 20
res = sc.resolution
print('res=', res)


# **********************定制类****************************
# 1.使用__str__
class Student2(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name, %s)' % self.name
        # __repr__ = __str__


print(Student2('小萌猴'))  # 返回Student object (name, 小萌猴)

s2 = Student2("小黑")
print('s2=', s2)


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):  # 实现一个__iter__()方法，该方法返回一个迭代对象
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a


for n in Fib():  # Fib()看起来和List有点儿像，但是不是List,如用下标取：Fib()[5]会报错
    print('n=', n)


class Fib1(object):
    def __getitem__(self, item):  # 实现__getitem__方法就可以用下标取了
        a, b = 1, 1
        for x in range(item):
            a, b = b, a + b
        return a


f1 = Fib1()
print('用下标取f1()=', f1[5])


# f1进行切片操作会报错，原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
class Fib2(object):
    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
                return a
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            l = []
            for x in range(stop):
                if x >= start:
                    l.append(a)
                a, b = b, a + b
            return l


f2 = Fib2()
print('f2进行切片操作:', f2[0:5])  # 从零开始取，取5个元素


class Students(object):
    def __init__(self):
        self.name = '小萌猴'


ss = Students()
print('ss对象的name属性：', ss.name)  # 如果打印ss.score，会报错，no attribute 'score'


class Students1(object):
    def __init__(self):
        self.name = '小萌猴'

    def __getattr__(self, item):
        if item == 'score':
            return 99


ss1 = Students1()
print('ss1对象的score属性：', ss1.score)  # 如果打印ss1.age，会返回None


class Students2(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


ss2 = Students2('cat')
print(ss2())  # ss2为对象，而在类中实现了__call__，可以当做函数调用（对象直接被调用）

# ***********************使用枚举类*****************************
from enum import Enum

# Month类型的枚举类
Month = Enum('month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print('Month的枚举：', Month.Feb.value)  # 直接使用Month.Jan来引用一个常量
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)  # value属性则是自动赋给成员的int常量，默认从1开始计数
print(type(Month))  # 返回<class 'enum.EnumMeta'>
print(isinstance(Month.Jan, Month))

# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类
from enum import unique


@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Mon
print('day1=', day1)  # day1返回Weekday.Mon
print(Weekday['Tue'])
print(Weekday(3))
print('星期四:', Weekday.Thu.value)


class A(object):
    def __init__(self):
        self.__private()
        self.public()

    def __private(self):
        print('A.__private()')

    def public(self):
        print('A.public()....')


class B(A):
    def __private(self):
        print('B.__private()')

    def public(self):
        print('B.public()++++')


print('B=', B())
# print('\n'.join(dir(A)))
