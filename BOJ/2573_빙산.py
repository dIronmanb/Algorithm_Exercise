'''
    시간 초과
    Recursion Error
'''

import sys
read = sys.stdin.readline

# 입력
dx = [-1,  1,  0,  0] 
dy = [ 0,  0, -1,  1]
y, x = [int(i) for i in read().split()]

iceberg = []
melted_ice = []

# Create and iceberg and melted_iceberg
for j in range(y):
    iceberg.append([int(i) for i in read().split()])
    melted_ice.append([0 for _ in range(x)])


       
# 빙산이 녹는 과정의 알고리즘
def melt_ice(iceberg):
    for j in range(1, y-1):
        for i in range(1, x-1):
            for a in range(4):
                ny = j + dy[a]
                nx = i + dx[a]
                
                if iceberg[ny][nx] == 0:
                    # 이미 여기서 melted_ice의 정보가 담겨 있다.
                    melted_ice[j][i] += 1
            
    for j in range(y):
        for i in range(x):
            iceberg[j][i] -= melted_ice[j][i]
            if iceberg[j][i] < 0:
                iceberg[j][i] = 0

# dfs로 빙산 개수 카운트
def dfs(root):
    
    stack = [root] # (y,x) 좌표를 의미함

    while(stack):

        node = stack.pop()
        melted_ice[node[0]][node[1]] = 0
        
        for i in range(4):
            ny = node[0] + dy[i]
            nx = node[1] + dx[i]
            
            if (0 <= nx < x) and (0 <= ny < y) and (melted_ice[ny][nx] != 0):
                stack.append((ny,nx))


loop_flag = True
iterate = 0
while loop_flag:
    iterate += 1
    
    melt_ice(iceberg)
    
    cnt = 0
    for j in range(1, y - 1):
        for i in range(1, x - 1):
            if melted_ice[j][i] != 0:
                dfs((j, i))
                cnt += 1
                
    if cnt == 1:
        iceberg_flag = True
        for j in range(y):
            for i in range(x):
                if iceberg[j][i] != 0:
                    iceberg_flag = False
                    break
                
        if iceberg_flag:
            print("Completely melted")
            break
        else:
            print("Not splited")
        
    else:
        print("Splited into {} parts".format(cnt))
        break
        
# print("\n\n")
# print("Program has been terminated")
# print("iterate: {}".format(iterate))
print(iterate)

