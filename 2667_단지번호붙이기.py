# -*- coding: utf-8 -*-
import sys
read = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0,  0, 1,-1]

def dfs(y, x):
    
    complex[y][x] = 0
    global house_count
    house_count += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < N) and (0 <= ny < N) and complex[ny][nx] == 1:
            dfs(ny,nx)




# Create complex map
N = int(read().strip())
complex = [list(map(int, read().strip())) for _ in range(N)]


#dfs
complex_list = []
house_count = 0
complex_count = 0
for j in range(N):
    for i in range(N):
        if complex[j][i] == 1:
            dfs(j,i)
            complex_count += 1
            complex_list.append(house_count)
            house_count = 0

complex_list.sort()
print(complex_count)
for a in complex_list:
    print(a)
            