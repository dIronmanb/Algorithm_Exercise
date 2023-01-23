# 구간 합 구하기 4

import sys
read = sys.stdin.readline

cals = []
N, M = list(map(int, input().split(' ')))
nums = [int(i) for i in read().split()]
acc = [0] * (N+1)

for i in range(M):
    cals.append([int(i) for i in read().split()])

for i in range(1, len(nums)+1):
    acc[i] = acc[i-1] + nums[i-1]

for i in range(M):
    print(acc[cals[i][1]] - acc[cals[i][0]-1])
    # print(sum(nums[cals[i][0]-1:cals[i][1]]))

