# -*- coding: utf-8 -*-
# @Author  : 不温卜火
# @Time    : 2022/9/18 18:55
# @Myblog  : https://buwenbuhuo.blog.csdn.net/

def list_mt():
    """
    列表举例
    :return:
    """
    # 列表
    lists=['a','b','c']
    lists.append('d')
    print(lists)
    print(len(lists))
    # 插入
    lists.insert(0,'len')
    lists.pop()
    print(lists)

if __name__ == '__main__':
    list_mt()