# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/2/19 下午2:09


import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

print('type of Card:', type(Card))


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]
        print(self._cards)
        print('_cards类型', isinstance(self._cards, list))

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


# print(Card)
beer_card = Card('7', 'diamonds')
print(isinstance(beer_card, tuple))
print(beer_card)

deck = FrenchDeck()
print(deck)
