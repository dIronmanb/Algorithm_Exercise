import sys
from collections import deque
read = sys.stdin.readline

A = read().rstrip()
T = deque(read().rstrip())

front = deque()
back = deque()

left = 0
right = len(T) - 1

while left < right:
    
    while left <= right:
        left += 1
        front.append(T.popleft())
        if len(front) >= len(A):
            flag = True
            i = 0
            while i < len(A):
                if A[len(A) - 1 - i] == front[len(front) - 1 - i]:
                    i += 1
                else:
                    flag = False
                    break
            if flag:
                for i in range(len(A)): front.pop()
                break

    while left <= right:
        right -= 1
        back.append(T.pop())
        if len(back) >= len(A):
            flag = True
            i = 0
            while i < len(A):
                if A[i] == back[len(back) - 1 - i]:
                    i += 1 
                else:
                    flag = False
                    break
            if flag:
                for i in range(len(A)): back.pop()
                break


result = []
for i in range(len(front)):
    result.append(front.popleft())
for i in range(len(back)):
    result.append(back.pop())

ti = 0
while ti >= 0:
    ti = ''.join(result).find(A)
    if ti != -1:
        del result[ti:ti+len(A)]

print(''.join(result))
