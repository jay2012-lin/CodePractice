# -*- coding: utf-8 -*-
# @Time    : 2018/3/5 下午11:53
# @Author  : jaylin
# @Email   : jaylin008@qq.com
# @File    : wangyi_xingyundaizi.py
# @Software: PyCharm
# 幸运袋子  动态规划
def composite(array, Sum, multiply):
    count = 0
    for i in range(len(array)):
        if i > 0 and array[i] == array[i - 1]:
            continue
        Sum += array[i]
        multiply *= array[i]
        if Sum > multiply:
            count += 1 + composite(array[i + 1:], Sum, multiply)
        elif array[i] == 1:
            count += composite(array[i + 1:], Sum, multiply)
        else:
            break
        Sum -= array[i]
        multiply /= array[i]
    return count


if __name__ == "__main__":
    n = input()
    array = raw_input().split()
    array = [int(i) for i in array]
    array.sort()
    print composite(array, 0, 1)