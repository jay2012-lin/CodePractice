# -*- coding: utf-8 -*-
# @Time    : 2018/2/28 9:13
# @Author  : jaylin
# @Email   : jaylin008@qq.com
# @File    : wangyi_fentiandi2.py
# @Software: PyCharm Community Edition

line1 = raw_input().strip().split()
n = int(line1[0])
m = int(line1[1])
lands = []
for i in range(n):
    line = raw_input().strip()
    li = [0] * (m + 1)
    for j in range(1, m + 1):
        li[j] = li[j - 1] + int(line[j - 1])
    lands.append(li)
D_c = [0]
for j in range(1, m + 1):
    D_c.append(sum(lands[i][j] for i in range(n)))
l = 0
r = int(D_c[m] / 16) + 1


def check(xpoint):
    j1_flag = 0
    for j1 in range(1, m - 2):
        if j1_flag == 0:
            if D_c[j1] < xpoint * 4:
                continue
            else:
                j1_flag = 1
        j2_flag = 0
        for j2 in range(j1 + 1, m - 1):
            if j2_flag == 0:
                if D_c[j2] - D_c[j1] < xpoint * 4:
                    continue
                else:
                    j2_flag = 1
            j3_flag = 0
            for j3 in range(j2 + 1, m):
                if j3_flag == 0:
                    if D_c[j3] - D_c[j2] < xpoint * 4:  # 以上几个判断都是寻找水平切割线
                        continue
                    else:
                        j3_flag = 1
                if D_c[m] - D_c[j3] < xpoint * 4:
                    break
                k = 0
                i = -1
                # 判断是竖直方向上能否被分成四个,并且都大于等于xpoint
                while k < 4:
                    dsum = [0, 0, 0, 0]
                    while dsum[0] < xpoint or dsum[1] < xpoint or dsum[2] < xpoint or dsum[3] < xpoint:
                        i += 1
                        if i == n:
                            break
                        dsum[0] += lands[i][j1]
                        dsum[1] += lands[i][j2] - lands[i][j1]
                        dsum[2] += lands[i][j3] - lands[i][j2]
                        dsum[3] += lands[i][m] - lands[i][j3]
                    else:
                        k += 1
                        continue
                    break
                else:
                    return 1
    return 0


while r - l > 1:
    x = int((r + l) / 2)
    if check(x):
        l = x
    else:
        r = x
print(l)