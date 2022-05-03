import sys
read = sys.stdin.readline

# 입력
dx = [-1,  1,  0,  0] 
dy = [ 0,  0, -1,  1]
y, x = [int(i) for i in read().split()]
iceberg = []
melted_ice = []
for j in range(y):
    iceberg.append([int(i) for i in read().split()])
    melted_ice.append([0 for _ in range(x)])

# 빙산이 녹는 과정의 알고리즘
def melt_ice(iceberg):
    for j in range(y):
        for i in range(x):
            for a in range(4):
                ny = j + dy[a]
                nx = i + dx[a]
                
                if 0 <= ny < y - 1 and 0 <= nx < x - 1 and iceberg[ny][nx] == 0:
                    melted_ice[j][i] += 1
            
    for j in range(y):
        for i in range(x):
            if iceberg[j][i] != 0:
                iceberg[j][i] -= melted_ice[j][i]
                if iceberg[j][i] < 0:
                    iceberg[j][i] = 0
            # 얼음 초기화
            melted_ice[j][i] = 0

i = 1
while i < 5:
    print("{} >>> ".format(i))
    for a in iceberg:
        print(a)
        
    melt_ice(iceberg)
    i += 1
    
# 두 개로 분리가 되는지 판별하는 알고리즘

