# -*- coding: utf-8 -*-
# @Author  : 不温卜火
# @Time    : 2022/9/18 19:07
# @Myblog  : https://buwenbuhuo.blog.csdn.net/


score = {'guanyu':95,'zhangfei':96}
#添加一个元素
score['zhaoyun'] = 98
print(score)

#删除一个元素
score.pop('zhangfei')

#查看key是否存在
if 'guanyu' in score:
    print('yes')
else:
    print('no')

#查看一个key对应的值
print(score.get('guanyu'))
print(score.get('yase',99))