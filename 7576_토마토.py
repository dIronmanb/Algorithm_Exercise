# -*- coding: utf-8 -*-
# 작업 중....
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10000)


def dfs(x: int, y: int)->None:
    dx = [1, -1,  0,  0]
    dy = [0,  0,  1, -1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # The tomatoes that are adjacent to each other are ripe.
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            graph[nx][ny] = 1
            



m, n = [int(i) for i in read().split()]
graph = []
empty = 0


for i in range(n):
    graph.append([int(a) for a in read().split()])
    # Sum empty spaces
    empty += graph[i].count(-1)

days = 0
pre_tomatoes = 0
while True:
    present_tomatoes = 0
    for i in range(n):
        for j in range(m):
            # If the tomatoes are ripe at that location,
            if graph[i][j] == 1:
                present_tomatoes += 1
                dfs(i,j)
                
    
    # If there is no difference in the number of ripe tomatoes from the previous day and today
    if(present_tomatoes == pre_tomatoes):
        break

    # When all the tomatoes have been already ripe
    elif(m * n + empty - present_tomatoes == 0):
        break

    else:
        pre_tomatoes = present_tomatoes
        days += 1

# When all the tomatoes are ripe
if(m * n + empty - present_tomatoes == 0):
      print(days)
# Otherwise
else:
    print(-1)


    

