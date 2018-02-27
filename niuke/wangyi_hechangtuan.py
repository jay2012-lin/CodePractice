# -*- coding: utf-8 -*-
# https://www.nowcoder.com/ta/2017test
n = int(raw_input())
a = raw_input().strip().split()
# print a  # ['7', '4', '7']
a = list(map(int,a))  # 对a中的所有元素map操作
# print a  # [7, 4, 7]
a.insert(0,0)
kd = raw_input().strip().split()
kd = list(map(int,kd))
K = kd[0]
D = kd[1]

# 行数为0和列数为0的元素都赋值为0不去考虑，可以看作下标从1开始
# 初始化0矩阵  (K+1) * (n+1)
fm = [[0]*(n+1) for i in range(K+1)]
fn = [[0]*(n+1) for i in range(K+1)]

# 使用动态规划，从最后一个元素入手
# fm[k][i]表示以a[i]为最后一个元素，选取k个学生所能达到的最大乘积
# fn[k][i]表示以a[i]为最后一个元素，选取k个学生所能达到的最小乘积
# 这儿也需要最小乘积，因为会有负数的存在
for i in range(1,n+1):
    fm[1][i] = a[i]
    fn[1][i] = a[i]


res = 0
for i in range(1,n+1):
    for k in range(2,K+1):
        for j in range(i-1,max(i-D,0)-1,-1):  # 从后往前遍历
            fm[k][i] = max(fm[k][i],fm[k-1][j]*a[i],fn[k-1][j]*a[i])
            fn[k][i] = min(fn[k][i],fm[k-1][j]*a[i],fn[k-1][j]*a[i])
    res = max(res,fm[K][i])

print(res)
