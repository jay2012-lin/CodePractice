# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 下午11:38
# @Author  : jaylin
# @Email   : jaylin008@qq.com
# @File    : wangyi_buyaoer.py
# @Software: PyCharm
# 数学问题  分为 整除4，整除2，奇数等几种情况讨论即可。蛋糕位置就是间隔每个2*2的正方形的区域。
# 解释 https://www.nowcoder.com/profile/3899811/codeBookDetail?submissionId=10419870
wh = raw_input().split()
w = int(wh[0])
h = int(wh[1])

def gen_cake_num(w,h):
    n = 0
    if (w % 4 == 0 or h % 4 == 0):
        n = w * h / 2
    elif (w % 2 == 0 and h % 2 == 0):
        n = (w * h / 4 + 1) * 2
    else:
        n = w * h / 2+1
    return n

print gen_cake_num(w,h)