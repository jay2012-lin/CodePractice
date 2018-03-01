# -*- coding: utf-8 -*-
# @Time    : 2018/3/1 8:39
# @Author  : jaylin
# @Email   : jaylin008@qq.com
# @File    : wangyi_hunheyanliao.py
# @Software: PyCharm Community Edition
import copy
n = int(raw_input())
X = raw_input().split()
X = [int(item) for item in X]
# X.sort(reverse=False)

def solve():
    # 不能构成dp问题的假设，这条思路错误
    X.sort()
    num_list = [0] * n
    buy_list = [[]] * n
    for i in range(n):
        if i == 0:
            buy_list[i] = [X[0]]
            num_list[i] = 1
            continue
        tempX = X[i]
        pre_buy_list = buy_list[i-1]
        pre_num = num_list[i-1]
        now_buy_list = copy.copy(pre_buy_list)
        now_buy_list.append(tempX)  # 直接append后面的数还是对应的异或数都不尽相同
        nowNum = pre_num + 1
        for item in pre_buy_list:
            tempNum = 10 ** 9 + 1
            temp_buy_list = []
            a = item ^ tempX
            if a in pre_buy_list:
                temp_buy_list = copy.copy(pre_buy_list)
                tempNum = pre_num

            if tempNum <= nowNum:
                nowNum = tempNum
                now_buy_list = temp_buy_list

        buy_list[i] = now_buy_list
        num_list[i] = nowNum

    return num_list[-1]

def solve2():
    '''
    使用矩阵秩的思想
    :return:
    '''
    for i in range(n-1,0,-1):
        # X[:i+1].sort()  # 在这儿要求排序,
        # python列表切片操作会返回一个新的列表，并赋予新的地址空间
        X.sort()  # 在这儿要求排序，这样写肯定正确，耗时
        for j in range(i-1,-1,-1):
            a = X[i] ^ X[j]
            if a < X[j]:
                X[j] = a  # 替换小的，将0置换到最上层，达到求秩的目的

    i = 0
    while X[i] == 0:
        i += 1
    return n - i

print solve()
