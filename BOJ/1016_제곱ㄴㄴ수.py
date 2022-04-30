from timeit import default_timer as timer

Min, Max = [int(i) for i in input().split()]

if 



# def isSquare(x):
#     if x < 4:
#         return False, 0
#     i = 2
#     while i**2 <= x:
#         if x % (i ** 2) == 0:
#             return True, i
#         i += 1
#     return False, 0



# start = timer()

# nums = [False for _ in range(Min, Max + 1)]
# #print(nums.keys())
# for i in range(Min, Max + 1):
#     if nums[i - Min]:
#         continue
        
#     truth, a = isSquare(i)
    
#     if truth:
#         pass

# # nums = {i: False for i in range(Min, Max)}
# # #print(nums.keys())
# # for i in nums.keys():
# #     if nums[i]:
# #         continue
        
# #     if isSquare(i):
# #         nums[i] = True

# # print(nums.values())
# # num = sum(nums.values())
# num = sum(nums)
# print(Max - Min + 1 - num)
# print(timer() - start)

         

      