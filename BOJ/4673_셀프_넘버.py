# -*- coding: utf-8 -*-

def digits(num):
    return [int(i) for i in str(num)]

LIMIT = 50
nums = [0 for _ in range(LIMIT + 1)]

for i in range(1, LIMIT + 1):
    if nums[i] == 0:
        print(i)        
        nums[i] = 1
        tmp = i

        while True:
            a = tmp + sum(digits(tmp))
            if a > LIMIT:
                break
            nums[a] = 1
            tmp = a

# def digits(num:int)->list:
#     return [int(i) for i in str(num)]

# def DP(i:int)->None:
#     tmp = i + sum(digits(i))
#     if tmp < LIMIT:
#         nums[tmp] = 1
#         DP(tmp)

# LIMIT = 50

# nums = [0 for _ in range(LIMIT)]

# for i in range(LIMIT):
#     if nums[i] == 0:
#         print(i)
#         nums[i] = 1
#         DP(i)


