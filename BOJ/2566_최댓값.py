# 9x9 격자판에 쓰여진 81개의 자연수 or 0
# 최댓값이 어디에 있는지 맞추는 문제

import sys
read = sys.stdin.readline

length = 9
board = [[] for i in range(length)]

for i in range(length):
    board[i].extend([int(a) for a in read().split()])

row, col = 0, 0
maximum = board[col][row]

for j in range(length):
    for i in range(length):
        if maximum < board[j][i]:
            maximum = board[j][i]
            col = j
            row = i

print(maximum)
print(col+1, row+1)