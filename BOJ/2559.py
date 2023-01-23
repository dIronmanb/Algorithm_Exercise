import sys
read = sys.stdin.readline

N, K = list(map(int, input().split(' ')))
dates = [int(i) for i in read().split()]

result = [0] * (N-(K-1))
result[0] = sum(dates[0:K])
for i in range(N-K):
    result[i+1] = result[i] - dates[i] + dates[i+K]

print(max(result))