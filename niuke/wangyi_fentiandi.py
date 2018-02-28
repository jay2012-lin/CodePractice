# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 17:21
# @Author  : jaylin
# @Email   : jaylin008@qq.com
# @File    : wangyi_fentiandi.py
# @Software: PyCharm Community Edition
# 思路是二分寻找答案，二分里面判断是否符合条件
# 根据c++版本改编的，提交上去出错，运行超时，原因应该是：c++效率高，该程序二分的范围大
# 第二个程序提交上去是正确的
nm = raw_input().strip().split()
n, m = int(nm[0]), int(nm[1])
values = [raw_input().strip() for i in range(n)]
values = [[int(value[i]) for i in range(m)] for value in values]  # 索引0开始
# print n,m
# print values

# sum = [[0] *(m+1)] * (n+1)  # 每个位置的表示左上角到该位置的和，索引0无意义
# 不能这样使用，类似于浅拷贝
sum = []
for i in range(n+1):
    sum.append([0] *(m+1))

for i in range(1,n+1):
    for j in range(1,m+1):
        sum[i][j] = sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1] + values[i-1][j-1]

# print sum

def calc(x, y, i, j):  # (i,j)到(x,y)之间的和
    return sum[x][y] - sum[x][j] - sum[i][y] + sum[i][j]

def judge(x):  # 判断以x为最小值时，能否横切成四份
    for i in range(1,m-2):  # 后面切一刀 下标从1开始
        for j in range(i+1,m-1):
            for k in range(j+1,m):
                last = 0;cnt = 0  # last 表示横向上一个切面的位置
                for r in range(1,n+1):  # 横向遍历
                    # 四个纵向计算
                    s1 = calc(r,i,last,0)
                    s2 = calc(r,j,last,i)
                    s3 = calc(r,k,last,j)
                    s4 = calc(r,m,last,k)

                    if (s1 >= x and s2 >= x and s3 >= x and s4 >= x):  # 这个判断保证最小
                        last = r  # 接着以上判断，因为是横切
                        cnt+=1

                if cnt >=4:
                    return True

    return False

left = 0
right = sum[n][m]
ans = 0
while(left <= right):
    # print left,right
    mid = (left+right) >> 1  # 除以2
    if judge(mid):
        left = mid + 1  # 保证最大
        ans = mid
    else:
        right = mid -1

print ans


# c++ 版本
# #include <cstdio>
# #include <cstring>
# #include <algorithm>
# #include <iostream>
# using namespace std;
# const int N = 10010;
# char str[100];
# int a[110][110];
# int sum[110][110], n, m;
# int calc(int x, int y, int i, int j){
#     return sum[x][y] - sum[x][j] - sum[i][y] + sum[i][j];
# }
# bool judge(int x){
#    for(int i = 1; i <= m - 3; i++)
#    {
#        for(int j = i + 1; j <= m - 2; j++)
#        {
#            for(int k = j + 1; k <= m - 1; k++)
#            {
#                 int last = 0, cnt = 0;
#                 for(int r = 1; r <= n; r++){
#                     int s1 = calc(r, i, last, 0);
#                     int s2 = calc(r, j, last, i);
#                     int s3 = calc(r, k, last, j);
#                     int s4 = calc(r, m, last, k);
#                     if(s1 >= x && s2 >= x && s3 >= x && s4 >= x){
#                         last = r; cnt++;
#                     }
#                   //  printf("i = %d j = %d k = %d last = %d\n",i, j, k, last);
#                 }
#                 if(cnt >= 4)return true;
#            }
#        }
#    }
#    return false;
# }
# int main(){
#     while(scanf("%d%d", &n, &m) > 0){
#         for(int i = 1; i <= n; i++){
#             scanf("%s", str + 1);
#             for(int j = 1; j <= m; j++){
#                 a[i][j] = str[j] - '0';
#             }
#         }
#         memset(sum, 0, sizeof sum);
#         for(int i = 1; i <= n; i++){
#             for(int j = 1; j <= m; j++){
#                 sum[i][j] = sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1] + a[i][j];
#             }
#         }
#         int l = 0, r = sum[n][m], ans = 0;
#         while(l <= r){
#             int m = (l + r) >> 1;
#             if(judge(m)){
#                 l = m + 1;
#                 ans = m;
#             }
#             else r = m - 1;
#         }
#         printf("%d\n", ans);
#     }
# }