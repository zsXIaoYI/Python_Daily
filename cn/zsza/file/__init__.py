# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2018/12/19 下午7:54

# with open('/PyCharm_Space/PythonDaily/test/1.txt', 'w') as f:
#     print('中国', file=f)


text_io = open('test.txt', 'wt')
text_io.write('咋哈哈哈')


s = u'中文'
f = open('test1.txt', 'w')
f.write(s)
f.close()


