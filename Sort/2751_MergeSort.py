# -*- coding: utf-8 -*-
'''
 시간 초과...
'''
def merge(L, R):

    i = 0
    j = 0

    sort_list = []
    
    while(i < len(L) and j < len(R)):

        if(L[i] < R[j]):
            sort_list.append(L[i])
            i += 1
        else:
            sort_list.append(R[j])
            j += 1
    
    # 나머지 남은 것들 채우기
    while(i < len(L)):
        sort_list.append(L[i])
        i += 1

    while(j < len(R)):
        sort_list.append(R[j])
        j += 1

    return sort_list




def merge_sort(data):
    
    length = len(data)
    middle = length // 2

    if(length <= 1):
        return data

    else:
        L = data[       :middle ]
        R = data[middle :       ]

        L1 = merge_sort(L)
        R1 = merge_sort(R)
        
        return merge(L1, R1)
 
    



N = int(input())
nums = []


for i in range(N):
    nums.append(int(input()))
    

nums = merge_sort(nums)


for i in range(N):
    print(i)
