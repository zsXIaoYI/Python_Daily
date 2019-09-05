# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/7/19 上午11:02


import pyperclip

# 逗号当做空格分割字符串
print('hello nice,', 'I am in Beijing')

print('I\'m ok!')
# 字符串前面加r，进行转义
print(r'I\'m ok!')

s1 = 'zs123bj'
# 判断某个子串是否在字符串中
print('12' in s1)

l1 = ['a', 'b', 'c']
# 用横线连接list中的元素
print('-'.join(l1))

# 字符串是否只包含字母
print(s1.isalpha())

# 字符串是否只包含字母和数字
print(s1.isalnum())

# 字符串是否只包含数字
print(s1.isdecimal())

s2 = 'Giraffe Academy'
print('s2是否为全大写:', s2.isupper())


# 复制到系统剪切板
pyperclip.copy('something')


# 字符串一些反转方法
def reverse_str1(s):
    return s[::-1]


def reverse_str2(s):
    if len(s) <= 1:
        return s
    return reverse_str2(s[1:]) + s[0:1]


print(reverse_str1('abc'))
print(reverse_str2('abcd'))
