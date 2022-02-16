# -*- coding: utf-8 -*-
# 작업 중....

import sys
read = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x: int, y: int)->bool:

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    field[x][y] = False
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # Branch & Bound
        if 0 <= nx < width and 0 <= ny < height and field[nx][ny] == True:
            dfs(nx,ny)

            




test_nums = int(read())


for i in range(test_nums):
    width, height, cabbage_num = [int(i) for i in read().split()]
    earthwarms_num = 0

    #Create 2d list
    field = [[False] * height for _ in range(width)]

    # input cabbage
    for i in range(cabbage_num):
        x,y = [int(i) for i in read().split()]
        field[x][y] = True

    # dfs
    for i in range(width):
        for j in range(height):
            if field[i][j] == True:
                dfs(i,j)
                earthwarms_num += 1 
    print(earthwarms_num)   
