# -*- coding: utf-8 -*-
# @Author  : 不温卜火
# @Time    : 2022/9/18 19:37
# @Myblog  : https://buwenbuhuo.blog.csdn.net/

import numpy as np

a = np.array([1,2,3])

b = np.array([[1,2,3],[4,5,6],[7,8,9]])
# x y轴 [1,1] 代表修改的是b中的x、y坐标都为1的数
b[1,1] = 10

print(a)
print(b)