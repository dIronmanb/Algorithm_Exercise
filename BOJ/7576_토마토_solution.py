import sys
from collections import deque
read = sys.stdin.readline

field = []
days = 1
ripe_tomatoes = deque()

# input information
m, n = [int(i) for i in read().split()]
for i in range(n):
    field.append([int(a) for a in read().split()])

    # extract ripe tomatoes
    for j in range(len(field[i])):
        if field[i][j] == 1:
            ripe_tomatoes.append([i, j]) 



dx = [1, -1,  0,  0]
dy = [0,  0,  1, -1]
days = 0


while True:
    if len(ripe_tomatoes) == 0:
        break
    x,y = ripe_tomatoes.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == 0:
            field[nx][ny] = field[x][y] + 1
            ripe_tomatoes.append([nx,ny])
    

flag = False

for i in range(n):
    for j in range(m):
        if field[i][j] == 0:
            flag = True
            break

if flag:
    print(-1)
else:
    print(max([max(field[i]) for i in range(n)]) - 1)
    
