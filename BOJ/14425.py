# 문자열 집합

# 일일히 비교하는 건 시간이 너무 오래 걸린다

# 입력시 해시로 만들어버리는 건 어떨까?
# 해시 만드는 법 찾아서 함수로 만들기 -> 그리고 실험해보기
import sys
read = sys.stdin.readline

N, M = [int(i) for i in input().split()]

S = []
test = []

for i in range(N):
    S.append(read().rstrip())

for i in range(M):
    test.append(read().rstrip())

cnt = 0
for i in test:
    if i in S:
        cnt += 1

print(cnt)