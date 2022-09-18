# -*- coding: utf-8 -*-
# @Author  : 不温卜火
# @Time    : 2022/9/18 19:21
# @Myblog  : https://buwenbuhuo.blog.csdn.net/


s = {'a', 'b', 'c'}
s.add('d')
s.remove('b')
print(s)

if 'c' in s:
    print('yes')
else:
    print('no')