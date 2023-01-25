# 빗물

import sys
read = sys.stdin.readline


H, W = list(map(int, input().split(' ')))
world = [[0 for _ in range(W)] for _ in range(W)]
blocks = [int(i) for i in read().split()]

# world로의 mapping
for i in range(W):
    for j in range(H):
        if blocks[i] > 0:
            blocks[i] -= 1
            world[j][i] = 1

for j in range(H):
    print(world[j])

cnt = 0
for j in range(H):
    temp = []
    for i in range(W):

        # 스택이 비어있는 경우
        if not temp:
            if world[j][i] == 0:
                pass
            else:
                temp.append(1)

        # 스택의 peak가 1인 경우
        elif temp[-1] == 1:
            if world[j][i] == 0:
                temp.append(0)
            elif world[j][i] == 1:
                pass

        # 스택의 peak가 0인 경우
        elif temp[-1] == 0:
            if world[j][i] == 0:
                temp.append(0)
            elif world[j][i] == 1:
                while temp:
                    cnt += 1
                    temp.pop()
                cnt -= 1
                temp.append(1)

print(cnt)