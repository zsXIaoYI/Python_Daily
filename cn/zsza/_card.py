# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/2/19 下午2:09


# import collections

from collections import namedtuple
# 黑桃：Spades
# 红桃：Heart
# 方块：Diamond
# 梅花：Club
Card = namedtuple('Card', ['rank', 'suit'])

print('type of Card:', type(Card))


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]
        print('cards:', self._cards)
        print('cards类型是否为list:', isinstance(self._cards, list))

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


# print(Card)
beer_card = Card('7', 'diamonds')
print('beer_card类型:', isinstance(beer_card, tuple))
print('beer_card:', beer_card)

deck = FrenchDeck()
print(deck)

print('\n*************************\n')

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'Japan', '36.93', (36.58, 139.69))
print('tokyo:', tokyo)
print('东京人口:', tokyo.population)

print('City类的属性:', City._fields)

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'Indian', 21.93, LatLong(28.61, 77.20))

# 用_make()通过接受一个可迭代对象生成这个类的一个示例，它作用跟City(*delhi_data)是一样的
delhi = City._make(delhi_data)
print('delhi:', delhi)

print('delhi _asdict:', delhi._asdict())

for key, value in delhi._asdict().items():
    print(key + ':',  value)
