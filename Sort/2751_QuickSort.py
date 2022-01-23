# -*- coding: utf-8 -*-
# 채점중....
'''
 시간 초과
 빠른 정렬 알고리즘 필요: 퀵 sort 
 But... 퀵정렬의 경우에는 최악의 경우 n^2가 소요된다. >> Merge로 해보자
'''


def partitionQuickSort(data, start, end):
    
    left = start
    right = end
    pivot = start # pivot을 중앙으로 할 수는 없을까??
    
    while(left < right):
        while(data[left] < data[pivot] and left < right):
            left += 1
        while(data[right] >= data[pivot] and left < right):
            right -= 1

        if(left <= right):#left <= right
            data[left], data[right] = data[right], data[left]

    #left == right
    data[pivot], data[right] = data[right], data[pivot]
    
    return right

def quickSort(data, start, end):
    
    if(start < end):
        pivot = partitionQuickSort(data, start, end)
        quickSort(data, start, pivot-1)
        quickSort(data, pivot + 1, end)
    



N = int(input())
nums = []

for i in range(N):
    nums.append(int(input()))


quickSort(nums, 0, N-1)

for i in range(N):
    print(i)

#print(nums)

