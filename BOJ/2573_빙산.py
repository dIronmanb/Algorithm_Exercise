import sys
from copy import deepcopy
read = sys.stdin.readline
sys.setrecursionlimit(10000)

# 입력
dx = [-1,  1,  0,  0] 
dy = [ 0,  0, -1,  1]
y, x = [int(i) for i in read().split()]

iceberg = []
melted_ice = []
shape = []
visited = None


for j in range(y):
    iceberg.append([int(i) for i in read().split()])
    melted_ice.append([0 for _ in range(x)])
    shape.append([1 for _ in range(x)])


def renew_ice(visited):
    for j in range(y):
        for i in range(x):
            if iceberg[j][i] == 0:
                visited[j][i] = 0
        
# 빙산이 녹는 과정의 알고리즘
def melt_ice(iceberg):
    for j in range(1, y-1):
        for i in range(1, x-1):
            for a in range(4):
                ny = j + dy[a]
                nx = i + dx[a]
                
                if iceberg[ny][nx] == 0:
                    melted_ice[j][i] += 1
            
    for j in range(y):
        for i in range(x):
            iceberg[j][i] -= melted_ice[j][i]
            if iceberg[j][i] < 0:
                iceberg[j][i] = 0
            # 녹았던 얼음 초기화
            melted_ice[j][i] = 0

# dfs로 빙산 개수 카운트
def dfs(visited, y, x):
    visited[y][x] = 0
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if visited[ny][nx] == 1:
            dfs(visited, ny, nx)


loop_flag = True
iterate = 0
while loop_flag:
    iterate += 1
    
    melt_ice(iceberg)
    renew_ice(shape)
    visited = deepcopy(shape)
    
    cnt = 0
    for j in range(1, y - 1):
        for i in range(1, x - 1):
            if visited[j][i] == 1:
                dfs(visited, j, i)
                cnt += 1
                
    if cnt == 1:
        # print("Not splited")
        pass
    elif cnt == 0:
        # print("Completely melted")
        loop_flag = False
    else:
        # print("Splited into {} parts".format(cnt))
        break
        
# print("\n\n")
# print("Program has been terminated")
# print("iterate: {}".format(iterate))
print(iterate)

