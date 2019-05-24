# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/5/19 下午2:55

# 摄氏温度和华氏温度的转换
# F = 1.8C + 32

f = float(input('请输入华氏温度:\n'))
c = (f - 32) / 1.8

print('%.1f华氏度 = %.1f摄氏度' % (f, c))


"""
分段函数求值
        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
"""
x = float(input('x: \n'))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3

print('f(%.2f) = %.2f' % (x, y))

