# -*- coding: utf-8 -*-
# @Time    : 2018/3/1 11:26
# @Author  : jaylin
# @Email   : jaylin008@qq.com
# @File    : souhu_zuidashu.py
# @Software: PyCharm Community Edition
from collections import Counter
# line = raw_input()
# number = line.split()[0]
# cnt = int(line.split()[1])
numbers = raw_input()
cnt =  int(raw_input())

# numbers = [int(item) for item in numbers]
numbers = list(numbers)

def solve(numbers):
    # 从最小的开始删除，这种写法不对。
    # 例如：3540 删除一个 -> 354 显然错误
    count = Counter(numbers)
    count = sorted(count.iteritems(), key=lambda x: x[0], reverse=False)
    # print count
    remain_cnt = cnt  # 剩余的要删除的数
    for i, no in count:
        if remain_cnt <= 0:
            break
        remove_no = 0
        if remain_cnt >= no:
            remove_no = no
            remain_cnt = remain_cnt - no
        else:
            remove_no = remain_cnt
            remain_cnt = 0

        for j in range(remove_no):
            numbers.remove(i)

    number = [str(item) for item in numbers]
    return ''.join(number)

def solve2(numbers):
    # 从左至右，删除小于下一位的数，最后不够删除结尾数
    n, j, i = len(numbers), cnt, 0
    while j > 0 and i < n - 1:
        if numbers[i] >= numbers[i + 1]:
            i += 1
        else:
            numbers.pop(i)
            j -= 1
            n -= 1
            i = i - 1 if i > 0 else 0
    if j > 0:
        numbers = numbers[:-j]
    return ''.join(numbers)

print solve2(numbers)