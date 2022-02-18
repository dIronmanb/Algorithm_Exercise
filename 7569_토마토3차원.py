from re import L
import sys
from collections import deque
read = sys.stdin.readline

M, N, H = [int(i) for i in read().split()]
boxes = []
ripe_tomatoes = deque()
for h in range(H):
    one_box = []
    for n in range(N):
        one_box.append([int(i) for i in read().split()])
        # print(one_box)
        for m in range(M):
            if one_box[n][m] == 1:
                ripe_tomatoes.append([h, n, m])
    boxes.append(one_box)

# up,down,front,back,left,right
dx = [1, -1,  0,  0,  0,  0]
dy = [0,  0,  1, -1,  0,  0]
dz = [0,  0,  0,  0,  1, -1]

while True:
    print(ripe_tomatoes)
     
    if len(ripe_tomatoes) == 0:
        break
    
    z, y, x = ripe_tomatoes.popleft()
    for i in range(6):
        nz = z + dz[i]
        ny = y + dy[i]
        nx = x + dx[i]

        if (0 <= nz < H) and (0 <= ny < N) and (0 <= nx < M) and boxes[nz][ny][nx] == 0:
            boxes[nz][ny][nx] = boxes[z][y][x] + 1
            ripe_tomatoes.append([nz, ny, nx])
    
     
flag = True
maximum = deque()

for h in range(H):
    for n in range(N):
        maximum.append(max(boxes[h][n]))
        for m in range(M):
            if boxes[h][n][m] == 0:
                flag = False
                break
if flag:
    print(max(maximum) - 1)
else:
    print(-1)
    
    



