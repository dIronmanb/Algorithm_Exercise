N = input().rstrip()

nums = set([int(i) for i in N])
if 0 in nums:
    nums.remove(0)

# int형으로 변환
N = int(N)

# print(nums)

def judge(num, divisors):
    for i in divisors:
        if num % i != 0:
            return False
    return True


# # 648 -> 648
# if judge(N, nums):
#     print(N)
# else:
#     for i in range(10):
#         if judge(N*10+i, nums):
#             print(N*10+i)
#             break
#     else:
#         for i in range(100):
#             if judge(N*100+i, nums):
#                 print(N*100+i)
#                 break


dec = 1
flag = False
while True:
    for i in range(dec):
        if judge(N*dec+i, nums):
            print(N*dec+i)
            flag = True
            break
    if flag:
        break

    dec *= 10
