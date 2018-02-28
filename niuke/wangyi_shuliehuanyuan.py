# -*- coding: utf-8 -*-
# @Time    : 2018/2/28 13:27
# @Author  : jaylin
# @Email   : jaylin008@qq.com
# @File    : wangyi_shuliehuanyuan.py
# @Software: PyCharm Community Edition
# 思路：将空位置拿出来递归全排列，判断是否符合条件
line1 = raw_input().split()
n = int(line1[0])
k = int(line1[1])

a_array = raw_input().split()
a_array = [int(item) for item in a_array]
# print n,k,a_array

def sequence(n,k,a_array):

    def right_seq(pair_num,lost_loc,a_lost,a_array):
        '''第一个参数表示还剩余多少个顺序对'''
        if pair_num < 0 or (pair_num > 0 and len(lost_loc) <= 0):
            return 0
        if pair_num == 0 and len(lost_loc) == 0:
            return 1
        result = 0
        for i in range(len(a_lost)):  # 将缺失的数字填充到空位置
            add_position = lost_loc[0]
            a_array[add_position] = a_lost[i]  # 先赋值
            new_add = 0  # 新增加一个元素增加的的顺序对
            for j in range(n):
                if a_array[j] != 0 and ((j<add_position and a_array[j]<a_array[add_position])
                                        or (j>add_position and a_array[j]>a_array[add_position])):
                    new_add += 1
            result += right_seq(pair_num-new_add,lost_loc[1:],
                                a_lost[:i]+a_lost[i+1:],a_array)
            a_array[add_position] = 0  # 清零

        return result


    # 缺失的数据
    tempList = range(0,n+1)
    a_lost = list(set(tempList) - set(a_array))
    # print a_lost
    # print len(a_lost)

    # 缺失的位置
    lost_loc = []
    for i in range(n):
        if a_array[i] == 0:
            lost_loc.append(i)

    # print len(lost_loc)

    # 目前序列中已经存在的 顺序对
    existed_pair_num = 0
    for i in range(n-1):
        if a_array[i] != 0:
            for j in range(i+1,n):
                if a_array[j] > a_array[i]:
                    existed_pair_num += 1
    # print existed_pair_num

    return right_seq(k-existed_pair_num,lost_loc,a_lost,a_array)

print sequence(n,k,a_array)
