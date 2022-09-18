# -*- coding: utf-8 -*-
# @Author  : 不温卜火
# @Time    : 2022/9/18 17:29
# @Myblog  : https://buwenbuhuo.blog.csdn.net/


def scores(score):
    """
    定义一个函数scores，用来做判断
    :param score: 分数区间
    :return:
    """
    if score >= 90:
        print('Excellent')
    else:
        if score < 60:
            print('Fail')
        else:
            print('Good Job')

if __name__ == '__main__':
    scores(95)