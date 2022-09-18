# -*- coding: utf-8 -*-
# @Author  : 不温卜火
# @Time    : 2022/9/18 19:26
# @Myblog  : https://buwenbuhuo.blog.csdn.net/

"""
题目要求：
    INPUT
    1 5
    OUTPUT
    6
"""

while True:
    try:
        print("Please input numbers:")
        line = input()
        a = line.split()
        print(int(a[0]) + int(a[1]))
    except:
        break
