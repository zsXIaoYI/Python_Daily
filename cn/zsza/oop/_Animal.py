# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/2/15 下午9:22


class Animal(object):

    def run(self):
        print('is Running')


class Dog(Animal):
    pass


# Cat类覆写Animal的run方法
class Cat(Animal):

    def run(self):
        print('Cat  is  Running')


class Monkey(Animal):

    def run(self):
        print('Monkey is Running')


dog = Dog()
dog.run()

cat = Cat()
cat.run()


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Monkey())
