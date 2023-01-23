# 구간 합 구하기 5

import sys
read = sys.stdin.readline

N, M = list(map(int, input().split(' ')))

map2d = []
for i in range(N):
    map2d.append([int(j) for j in read().split()])

acc = [[0 for i in range(N+1)] for i in range(N+1)]

cals = []
for i in range(M):
    cals.append([int(i) for i in read().split()])

# Case 1
for j in range(1, N+1):
    for i in range(1, N+1):
        acc[j][i] = acc[j-1][i] + acc[j][i-1] + map2d[j-1][i-1]
        # 중복 빼주기
        acc[j][i] -= acc[j-1][i-1]

for x1, y1, x2, y2 in cals:
    # print(acc[y2][x2], acc[y1-1][x2], acc[y2][x1-1], acc[y1-1][x1-1])
    # print(acc[y2][x2] - acc[y1-1][x2] - acc[y2][x1-1] + acc[y1-1][x1-1])

    # 부호 어디선가 빗나감
    print(acc[x2][y2] - acc[x1-1][y2] - acc[x2][y1-1] + acc[x1-1][y1-1])

'''
# Case 2
for j in range(1, N+1):
    for i in range(1, N+1):
        acc[j][i] = acc[j][i-1] + map2d[j-1][i-1]
        
for i in range(1, N+1):
    for j in range(1, N+1):
        temp[j][i] = temp[j-1][i] + acc[j][i-1]
'''


# print
# for j in range(N):
#     print(map2d[j])
#
# print()
#
# for j in range(N+1):
#     print(acc[j])



