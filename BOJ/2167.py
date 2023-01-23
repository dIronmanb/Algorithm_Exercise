# 2차원 배열의 합 - 11660참고

# 구간 합 구하기 5

import sys

read = sys.stdin.readline

N, M = list(map(int, input().split(' ')))

map2d = []
for i in range(N):
    map2d.append([int(j) for j in read().split()])

acc = [[0 for i in range(M + 1)] for i in range(N + 1)]

cals = []

K = int(input())
for i in range(K):
    cals.append([int(i) for i in read().split()])

# Case 1
for j in range(1, N + 1):
    for i in range(1, M + 1):
        acc[j][i] = acc[j - 1][i] + acc[j][i - 1] + map2d[j - 1][i - 1]
        # 중복 빼주기
        acc[j][i] -= acc[j - 1][i - 1]

for x1, y1, x2, y2 in cals:

    # 부호 어디선가 빗나감
    print(acc[x2][y2] - acc[x1 - 1][y2] - acc[x2][y1 - 1] + acc[x1 - 1][y1 - 1])




