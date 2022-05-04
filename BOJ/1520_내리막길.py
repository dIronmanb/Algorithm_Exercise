import sys
# from timeit import default_timer as timer
read = sys.stdin.readline

dx = [1, -1,  0,  0]
dy = [0,  0,  1, -1]

# Input
y, x = [int(i) for i in read().split()]
cnt = 0

# make Map
map_list = [[] for _ in range(y)]
possible = [[-1 for _ in range(x)] for _ in range(y)]

for i in range(y):
    map_list[i].extend([int(i) for i in read().split()])


def dfs(b, a):

    if b == 0 and a == 0:
        return possible[b][a]        
        
    if possible == -1:
        # 방문 완료
        possible[b][a] = 0
        return possible[b][a]
            
    for i in range(4):
        ny = b + dy[i]
        nx = a + dx[i]
            
        if 0 <= nx < x and 0 <= ny < y and map_list[b][a] > map_list[ny][nx]:
            possible[ny][nx] = possible[b][a] + dfs(ny, nx)
            
    return possible[b][a] 
       
dfs(y-1, x-1)
for i in possible:
    print(i)
# print(timer() - start)
# 4.2588915675878525e-05
                 
                 