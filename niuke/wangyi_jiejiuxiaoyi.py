# -*- coding: utf-8 -*-
# @Time    : 2018/3/8 上午12:00
# @Author  : jaylin
# @Email   : jaylin008@qq.com
# @File    : wangyi_jiejiuxiaoyi.py
# @Software: PyCharm

n = int(raw_input())
x = map(int,raw_input().split())
y = map(int,raw_input().split())
z = []
for i in range(len(x)):
    temp = x[i] + y[i]
    z.append(temp)

z.sort()
print z[0] - 2