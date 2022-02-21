# -*- coding: utf-8 -*-
# 입력은 별로 많지 않아서 sys.stdin.readline은 생략
import sys
from collections import deque
read = sys.stdin.readline

def least_moment(val):
    if(val % 2 == 1):
        a.append(val+1)
        a.append(val-1)
    elif(val %2 == 0):
        a.append(val/2)


N, K = [int(i) for i in read().split()]

a = deque()

if K == N:
    print(0)
elif K < N:
    print(N-K)
else:
    count = 0
    least_moment(K)

    while True:
        for i in range(len(a)):
            val = a.popleft()
            if val == N:
                break
            least_moment(val)
        
        count += 1
        print(a)
        print(count)
        if val == N:
            break

    print(count)      
