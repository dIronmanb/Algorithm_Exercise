import sys
read = sys.stdin.readline


N = int(read())
t = []
p = []
reward = [0 for _ in range(N+1)]
result = 0

for i in range(N):
    days, pay = [int(i) for i in read().split()]
    t.append(days)
    p.append(days)


for i in range(N):
    if i + t[i] < N:
        reward[i + t[i]] = max(reward[i + t[i]] , reward[i] + p[i])
        result = max(result, reward[i + t[i]])

    reward[i + 1] = max(reward[i + 1], reward[i])
    result = max(result, reward[i + 1])

print(result)