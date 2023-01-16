# 피보나치 수 2
# Solution: Dynamic Programming
n = int(input())

temp = [0, 1]

for i in range(n-1):
    result = temp[0] + temp[1]
    temp[0], temp[1] = temp[1], result

if n == 1:
    print(1)
else:
    print(temp[1])