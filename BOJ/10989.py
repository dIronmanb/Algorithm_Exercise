# 수 정렬하기
# Solution: 해당되는 index를  1 증가시키기
import sys
read = sys.stdin.readline


nums = int(input())
num_list = [0] * 10001

for i in range(nums):
    num_list[int(read())] += 1

for idx, val in enumerate(num_list, start=0):
    if val == 0:
        continue
    else:
        for i in range(val):
            print(idx)

