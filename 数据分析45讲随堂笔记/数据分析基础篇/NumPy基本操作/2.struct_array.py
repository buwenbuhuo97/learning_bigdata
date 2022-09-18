# -*- coding: utf-8 -*-
# @Author  : 不温卜火
# @Time    : 2022/9/18 19:47
# @Myblog  : https://buwenbuhuo.blog.csdn.net/


import numpy as np

# dtype定义结构类型
persontype = np.dtype(
    {
    'names':['name', 'age', 'chinese', 'math', 'english'],
    'formats':['S32','i', 'i', 'i', 'f']
    }
)

peoples = np.array(
    [
     ("ZhangFei",32,75,100, 90),
     ("GuanYu",24,85,96,88.5),
     ("ZhaoYun",28,85,92,96.5),
     ("HuangZhong",29,65,85,100)
     ]
    ,dtype=persontype)

# 每个人的年龄
ages = peoples[:]['age']
# 每个人的语文成绩
chineses = peoples[:]['chinese']
# 每个人的数学成绩
maths = peoples[:]['math']
# 每个人的英语成绩
englishs = peoples[:]['english']


print(np.mean(ages))
print(np.mean(chineses))
print(np.mean(maths))
print(np.mean(englishs))