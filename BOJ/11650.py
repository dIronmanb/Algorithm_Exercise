# 좌표 정렬하기

import sys
read = sys.stdin.readline

N = int(input())
result = []
for i in range(N):
    result.append([int(i) for i in read().split()])

result.sort()
# result.sort(key=lambda x: (x[0], x[1]))와 동치
# result.sort(key=lambda x: (x[1], x[0]))은 y를 먼저 sort

for i in result:
    print(i[0], i[1])

