# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2020/2/18 11:35
# @File: _4.py
# __author__ = 'zs'


class Super:
    def method(self):
        print('in Super.method')
    '''
    action()方法存在于子类当中,这种写法是与Java不同的，Java语法不允许这样
    '''
    def delegate(self):
        self.action()


class Inheritor(Super):
    pass


class Replacer(Super):
    def method(self):
        print('in Replacer.method')


class Extender(Super):
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')


class Provider(Super):
    def action(self):
        print('in Provider.action')


if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()

    print('\n')
    x = Provider()
    x.delegate()
