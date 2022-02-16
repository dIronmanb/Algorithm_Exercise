# -*- coding: utf-8 -*-
# 작업 중....
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10000)

count = 0

def dfs(x: int, y: int)->int:
    global count
    blocked_count = 0
    dx = [1, -1,  0,  0]
    dy = [0,  0,  1, -1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # if the position state is 1, adjacent position states convert 0 to 1
        if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
            graph[nx][ny] = 1
            blocked_count = 0
            dfs(nx, ny)
        elif nx < 0 or nx >= m or ny < 0 or ny > n or (0 <= nx < m and 0 <= ny < n and (graph[nx][ny] == -1 or graph[nx][ny] == 1)):
            blocked_count += 1
            if blocked_count == 4:
                return -1

    return count


m, n = [int(i) for i in read().split()]
graph = []
for _ in range(n):
    graph.append([int(i) for i in read().split()])
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            val = dfs(i,j)
    
print(val)


    

