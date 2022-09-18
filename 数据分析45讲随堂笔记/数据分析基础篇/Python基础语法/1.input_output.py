# -*- coding: utf-8 -*-
# @Author  : 不温卜火
# @Time    : 2022/9/18 17:27
# @Myblog  : https://buwenbuhuo.blog.csdn.net/

def data(name,sum):
    """
    最基础的入门程序
    :param name: 姓名
    :param sum: 求和
    :return:
    """
    name = input("What's your name?\n")
    sum =200 + 50
    print('hello,%s' %name)
    print('sum = %d' %sum)

if __name__ == '__main__':
    data("",0)