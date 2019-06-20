# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/6/20 下午3:14

#  异常的处理

input_again = True
while input_again:
    try:
        a = int(input('a= '))
        b = int(input('b= '))
        print('%d / %d = %.2f' % (a, b, a / b))
        input_again = False
    # except ValueError as e:
    #     print('请输入整数 error is {} ', e)
    # except ZeroDivisionError:
    #     print('除数不能为零')

    # 上面注释代码可以写成这样
    except (ValueError, ZeroDivisionError) as msg:
        print('异常信息:', msg)
