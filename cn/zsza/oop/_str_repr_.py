# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/6/28 下午3:03


class Test(object):

    def __init__(self, value='test'):
        self._data = value


class TestRepr(Test):

    def __repr__(self):
        return 'TestRepr(%s)' % self._data


class TestStr(Test):

    def __str__(self):
        return '[Value: %s]' % self._data


tr = TestRepr()
# tr 交互式环境中,输入tr,和print打印一样
print('tr:', tr)

# 交互式环境中,输入_tr,和print打印不一样
_str = TestStr()
print('str:', _str)
