# -*- coding: utf-8 -*-
import sys
from collections import deque
read = sys.stdin.readline

A = read().rstrip()
T = read().rstrip()


left_stack = deque()
right_stack = deque()

low, high = 0, len(T) - 1

while low <= high:
    
    while low <= high:
        flag = False

        left_stack.append(T[low])
        low += 1

        if len(left_stack) >= len(A):
            flag = True
            for i in range(len(A)):
                if left_stack[len(left_stack) - len(A) + i] != A[i]:
                    flag = False
                    break
            if flag:
                for i in range(len(A)):
                    left_stack.pop()
                break
    
    while low <= high:
        flag = False

        right_stack.append(T[high])
        high -= 1

        if len(right_stack) >= len(A):
            flag = True
            for i in range(len(A)):
                if right_stack[i] != A[i]:
                    flag = False
                    break
            if flag:
                for i in range(len(A)):
                    right_stack.popleft()
                break

# print(left_stack)
# print(right_stack)
result = ""
for i in range(len(left_stack)):
    result += left_stack[i]
for i in range(len(right_stack)):
    result += right_stack[len(right_stack) - i - 1]

# print(result)
result = result.replace(A,"")
print(result)
