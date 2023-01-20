# 색종이
# Solution 해당 하는 영역에 False -> True로 (중복되면 pass)
import sys
read = sys.stdin.readline

# 색종이 개수
n = int(input())
color_paper_pos = []

# 도화지
paper = [[False for i in range (101)] for i in range(101)]

# 색종이를 붙인 위치
for i in range(n):
    x, y = [int(i) for i in read().split()]

    for j in range(y, y+10):
        for i in range(x, x+10):
            paper[j][i] = True

print(sum(sum(i) for i in paper))

