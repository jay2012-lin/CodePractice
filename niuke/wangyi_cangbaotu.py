# -*- coding: utf-8 -*-
# @Time    : 2018/2/28 13:16
# @Author  : jaylin
# @Email   : jaylin008@qq.com
# @File    : wangyi_cangbaotu.py
# @Software: PyCharm Community Edition

s = raw_input()
t = raw_input()

def judge():
    i = 0
    for j in range(len(s)):
        if s[j] == t[i]:
            i += 1
            if i >= len(t):
                break
    if i == len(t):
        return "Yes"
    else:
        return "No"

print judge()