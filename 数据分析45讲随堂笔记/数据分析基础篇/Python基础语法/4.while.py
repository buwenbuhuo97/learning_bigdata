# -*- coding: utf-8 -*-
# @Author  : 不温卜火
# @Time    : 2022/9/18 18:50
# @Myblog  : https://buwenbuhuo.blog.csdn.net/

def whiles(sum,number):
    """
    循环语句 while 举例
    :param sum:
    :param number:
    :return:
    """
    # sum = 0
    # number = 1
    while number < 11 :
        sum = sum + number
        number = number + 1
    print(sum)

if __name__ == '__main__':
    whiles(0,1)