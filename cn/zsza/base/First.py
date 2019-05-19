# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2018/11/8 下午1:14

print(11)
print(100 + 200)

print('hello nice,', 'I am in Beijing')
print('100 + 200 =', 100 + 200)

# name = input('please enter your name: \n')
# print('name:', name)

# if else 后面的冒号不能少
a = 100
if a >= 0:
    print(a)
else:
    print(-a)

print('I\'m ok!')

res = 3 > 2 and 5 > 6
print('res:', res)

# Python中除法的计算结果是浮点数，即使两个整数恰好整除，结果也是浮点数
r1 = 9 / 3
print('r1=', r1)

# 地板除,Python中的取整，取模运算和java一样
r2 = 10 // 3
print('r2=', r2)

s1 = r'hello, "kitty"'
# 打印多行字符串
s2 = r'''hello,              
lisa!'''
print('s1:', s1)
print('s2:', s2)

print('包含中文的str')

flag = None
print(flag is None)
print(flag is not None)

st1 = 'abc'
st_new = st1.replace('a', 'n')
print(st1)
print(st_new)

# 去除字符串的首尾空格
st2 = ' ab c '
print(len(st2.strip()))


st3 = 'abcde'
print(st3[:3])
print(st3[1:])

sp = 'a  b c'.split()   # 返回一个list
print(isinstance(sp, list))


print(b'\xF0\x9F\xA6\x90'.decode('utf-8'))
