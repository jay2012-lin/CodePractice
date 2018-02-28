# -*- coding: utf-8 -*-
# @Time    : 2018/2/28 12:57
# @Author  : jaylin
# @Email   : jaylin008@qq.com
# @File    : wangyi_fenpingguo.py
# @Software: PyCharm Community Edition

def main():
    n = int(raw_input())
    a = raw_input().split()
    a = [int(item) for item in a]

    a_sum = sum(a)
    if a_sum % n != 0:
        return -1
    a_mean = a_sum / n
    result = 0
    for item in a:
        a_diff = item - a_mean
        if a_diff % 2 != 0:
            return -1
        if a_diff > 0:
            result += a_diff / 2
    return result

print main()