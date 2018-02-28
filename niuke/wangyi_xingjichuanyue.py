# -*- coding: utf-8 -*-
# @Time    : 2018/2/28 13:07
# @Author  : jaylin
# @Email   : jaylin008@qq.com
# @File    : wangyi_xingjichuanyue.py
# @Software: PyCharm Community Edition
import math
h = int(raw_input())
# 使用一元二次方程解的公式
x = math.floor((math.sqrt(4*h+1)-1)/2)
print int(x)