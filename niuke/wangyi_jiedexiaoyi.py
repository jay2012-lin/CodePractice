# -*- coding: utf-8 -*-
# @Time    : 2018/3/8 20:26
# @Author  : jaylin
# @Email   : jaylin008@qq.com
# @File    : wangyi_jiedexiaoyi.py
# @Software: PyCharm Community Edition

x0 = int(raw_input())
divided = 1000000007

def get_num():  # 有错
    result_num = 0
    iter = 0
    node_list = [x0]
    while result_num <= 100000:
        if iter > 2 ^ (result_num)-1:
            result_num += 1
        node = node_list[0]
        if node % divided == 0:
            break
        else:
            left = node * 4 + 3
            right = node * 8 + 7
            node_list.append(left)
            node_list.append(right)
        node_list = node_list[1:]
        iter += 1

    if result_num == 100001:
        return -1
    return result_num

# 参考 http://blog.csdn.net/fcxxzux/article/details/52138964#t0
def get_num1():
    times = 4
    ans = 100001
    for i in range(1,300000+1):
        x=(x0 * times+times-1) % divided
        if x == 0:
            ans=(i+1) / 3+(1 if (i+1) % 3 else 0)  # 贪心取3
            break

        times = times * 2 % divided  # 同余的性质(暂时不明白)
        # times = times * 2  # 这样写错误

    if ans > 100000:
        return -1
    return ans


print get_num1()