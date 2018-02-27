# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 15:38
# @Author  : jaylin
# @Email   : jaylin008@qq.com
# @File    : wangyi_dilaotaotuo.py
# @Software: PyCharm Community Edition
# https://www.nowcoder.com/ta/2017test 第二题
def main():
    nm = raw_input().split()
    n, m = int(nm[0]), int(nm[1])

    path_matrix = [raw_input() for i in range(n)]

    x0_y0 = raw_input().split()
    x0,y0 = int(x0_y0[0]),int(x0_y0[1])

    k = int(raw_input())
    alternative_steps = [list(map(int,raw_input().split())) for i in range(k)]

    step_matrix = [[-1] * m for i in range(n)]  # 步数矩阵，记录到达位置的最短步数
    arrived_matrix = [[0] * m for i in range(n)]  # 到达矩阵，是否到达
    # 判断初始点
    if path_matrix[x0][y0] != '.':
        return -1

    arrived_matrix[x0][y0] = 1
    step_matrix[x0][y0] = 0
    current_points = [[x0,y0]]
    while len(current_points) > 0:
        next_points = []
        for point in current_points:
            x, y = point[0], point[1]
            for step in alternative_steps:
                x_, y_ = x + step[0], y + step[1]
                if x_ < 0 or x_ >= n or y_ < 0 or y_ >= m:  # 判断是否越界
                    continue
                if path_matrix[x_][y_] != '.' or arrived_matrix[x_][y_] == 1:  # 不能到达或者已经到达
                    continue
                else:
                    step_matrix[x_][y_] = step_matrix[x][y] + 1
                    arrived_matrix[x_][y_] = 1
                    next_points.append([x_,y_])
        current_points = next_points
    # 选取最大步数并且输出
    max_step = 0
    for i in range(n):
        for j in range(m):
            step = step_matrix[i][j]
            if step == -1 and path_matrix[i][j] == '.':  # 这儿的判断非常重要，表示不能到达
                return -1
            if step > max_step:
                max_step = step

    return max_step

print main()
