# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2018/11/24 下午7:39

# 字符转ASCII值
p1 = ord('A')
print('A的ASCII值为:', p1)

# ASCII值转字符
n1 = chr(66)
print('n1:', n1)

s1 = 'ABC'.encode('ascii')
print('s1:', s1)

s2 = '中文'.encode('utf-8')
print('s2:', s2)

# 解码
s3 = b'acv'.decode('ascii')
print('s3:', s3)

# 中文的utf-8编码进修解码
s4 = b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
print('解码:', s4)

# 计算字符串长度
l1 = len('csv')
print('l1:', l1)

l3 = len(b'\xe4\xb8\xad\xe6\x96\x87')
print('中文解码后占用的字节长度:', l3)
# 1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节

g1 = 72
g2 = 85
r = (g2 - g1) / g1 * 100
res = '{0}成绩提升了{1:.2f}%'.format('小明', r)
print(res)

#  input返回的类型是字符串，不能直接和整型比较
s = input('enter your birth: \n')
birth = int(s)
if birth < 2000:
    print('非00后')
else:
    print('00后')


r1 = abs(-12)
print('-12的绝对值:', r1)

r2 = max(1, -2, 3, 5)
print('最大值:', r2)

print('字符串转整型:', int('156'))
print('浮点型转整型:', int(12.36))
print('整型转换成字符串:', str(102))

