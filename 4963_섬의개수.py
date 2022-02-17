# -*- coding: utf-8 -*-
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10000)


def dfs(x,y):

    if not( (0<=x<height) and (0<= y <width)) or graph[x][y] == 0:
        return False
        
    if graph[x][y] == 1:
        graph[x][y] = 0
        #상하좌우 조사
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)

        #대각 성분도 조사
        dfs(x + 1, y + 1)
        dfs(x + 1, y - 1)
        dfs(x - 1, y + 1)
        dfs(x - 1, y - 1)
        return True
        
    return False


result = []
width, height = [int(i) for i in read().split()] #맵의 크기는 계산 중에 변하지 X
while (width, height) != (0,0):
    graph = []
    for i in range(height):
        graph.append([int(i) for i in read().split()])

    # DFS
    islands = 0
    # 먼저 height를 입력하고, width를 입력해야 한다.
    for i in range(height):
        for j in range(width):
            if dfs(i, j) == True:
                islands += 1
    
    
    result.append(islands)
    width, height = [int(i) for i in read().split()]


for i in result:
    print(i)
