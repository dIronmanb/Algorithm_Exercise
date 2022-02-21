# -*- coding: utf-8 -*-
# 입력은 별로 많지 않아서 sys.stdin.readline은 생략
import sys
from collections import deque
read = sys.stdin.readline
visited = [0] * 100001

def least_moment(val):
    if 0 <= val <= 100000:
        if visited[val] == 0:
            visited[val] = 1
            
            a.append(val + 1)
            a.append(val - 1)
            a.append(val * 2)
    else:
        pass


    
    


N, K = [int(i) for i in read().split()]

a = deque()

if K == N:
    print(0)
elif K < N:
    print(N-K)
else:
    count = -1
    position = N
    a.append(N)

    while position != K:
        count += 1
        for _ in range(len(a)):
            position = a.popleft()
            if position == K:
                break
            least_moment(position)

    print(count)
