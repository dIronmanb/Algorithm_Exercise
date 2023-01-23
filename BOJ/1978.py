# 소수 찾기
import sys
import math
read = sys.stdin.readline

def is_prime_number(x):

    if x == 1:
        return False

    sq_root = math.sqrt(x)
    for i in range(2, int(sq_root)+1): # +1를 왜 할까?
        if x % i == 0:
            return False
    return True

N = int(input())
nums = [int(i) for i in read().split()]

cnt = 0
for num in nums:
    if is_prime_number(num):
        cnt += 1

print(cnt)

