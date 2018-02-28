# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 17:13
# @Author  : jaylin
# @Email   : jaylin008@qq.com
# @File    : wangyi_xiachufang.py
# @Software: PyCharm Community Edition
# https://www.nowcoder.com/ta/2017test 第三题
import sys

try:
    all_food = []
    for line in sys.stdin:
        for food in line.split():
            all_food.append(food)

    print len(set(all_food))
except:
    pass

