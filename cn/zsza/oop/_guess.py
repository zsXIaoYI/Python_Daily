# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/5/28 上午11:32

# 猜字游戏
from random import randint


class GuessMachine(object):

    def __init__(self):
        self._answer = None
        self._counter = None
        self._hint = None

    def reset(self):
        self._answer = randint(1, 100)
        self._counter = 0
        self._hint = None

    def guess(self, your_answer):
        self._counter += 1
        if your_answer > self._answer:
            self._hint = '小一点'
        elif your_answer < self._answer:
            self._hint = '大一点'
        else:
            self._hint = 'you guess it'
            return True
        return False

    @property
    def counter(self):
        return self._counter

    @property
    def hint(self):
        return self._hint


if __name__ == '__main__':
    gm = GuessMachine()
    play_again = True

    while play_again:
        game_over = False
        gm.reset()
        while not game_over:
            input_str = input('请输入:\n')
            if not input_str.isdigit():
                print('请输入数字')
                continue
            your_answer = int(input_str)
            game_over = gm.guess(your_answer)
            print(gm.hint)
        if gm.counter > 7:
            print('次数超过了7次')
        play_again = input('\n再玩一次?(yes|no)') == 'yes'
