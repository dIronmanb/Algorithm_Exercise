import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # map함수를 쓰려면 파이썬 버전을 3.x로 바꾸어야 한다!
add = {}

for _ in range(N):
    site, ps = input().split()  # 사이트 비밀번호 >> split() 써서 각각 집어넣기
    add[site] = ps              # 사이트: 비밀번호


for _ in range(M):
    print(add[input().rstrip()])

# rstrip(): 인자로 전달된 문자를 string의 오른쪽에서 제거
# 해당 사이트에서의 공백들을 모두 제거 -> 순수 사이트 이름의 문자열만 입력받음
# 사이트 : 비밀번호 
#
#
#
