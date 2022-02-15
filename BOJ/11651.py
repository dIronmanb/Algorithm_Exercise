# -*- coding: utf-8 -*-
# 채점중....
'''
 시간 초과
 빠른 정렬 알고리즘 필요: 퀵 sort 
 >> sorted 함수를 이용하고, 대신에 C++에 병합정렬 구현하기
'''
N = int(input())
nums = []

for i in range(N):
    nums.append(list(map(int, input().split())))


for i in range(N - 1):
    min = i
    for j in range(i + 1, N):
        if(nums[min][1] > nums[j][1]):
            min = j
        elif(nums[min][1] == nums[j][1] and nums[min][0] > nums[j][0]):
            min = j
            
    temp = nums[min]
    nums[min] = nums[i]
    nums[i] = temp

for i in range(N):
    print("{} {}".format(nums[i][0], nums[i][1]))