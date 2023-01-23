# 부분 합

import sys
read = sys.stdin.readline

acc = [0] * 100001
N, S = [int(i) for i in read().split()]

# C++의 경우 입력하면서 누적합하는게 가능하나, python은 더 알아보기
seq = [int(i) for i in read().split()]

for i in range(len(seq)):
    acc[i+1] = acc[i] + seq[i]

left = 0
right = 1
smallest = 100000
# print(acc)

while (right != len(acc)-1 and left != len(acc)-2):
    if acc[right] - acc[left] >= S:
        if right - left < smallest:
            smallest = right-left
        left += 1
    else:
        right += 1

if smallest == 100000:
    print(0)
else:
    print(smallest)