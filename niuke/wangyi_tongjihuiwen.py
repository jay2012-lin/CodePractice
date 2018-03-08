# -*- coding: utf-8 -*-
# @Time    : 2018/3/8 20:10
# @Author  : jaylin
# @Email   : jaylin008@qq.com
# @File    : wangyi_tongjihuiwen.py
# @Software: PyCharm Community Edition

A = raw_input()
B = raw_input()


def get_huiwen_num():
    def is_huiwen(s):
        s_len = len(s)
        if s_len <= 1:
            return True
        if s[s_len - 1] != s[0]:
            return False
        else:
            return is_huiwen(s[1:s_len - 1])

    num = 0
    for i in range(len(A) + 1):
        temp_str = ""
        if i < len(A):
            temp_str = A[:i] + B + A[i:]
        else:
            temp_str = A[:i] + B
        if is_huiwen(temp_str):
            num += 1

    return num

def get_huiwen_num1():
    num = 0
    for i in range(len(A) + 1):
        ab = A[:i] + B + A[i:]  # 如果前面的界限超出，则返回空字符串，列表返回空列表
        if ab[::-1] == ab: # 判断一个序列是否是回文 经典
            num += 1
    return num

print get_huiwen_num()
