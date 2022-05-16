

# '''
#     시간 초과
#     Recursion Error
#     틀렸습니다.
# '''

# import sys
# read = sys.stdin.readline

# # 입력
# dx = [-1,  1,  0,  0] 
# dy = [ 0,  0, -1,  1]
# y, x = [int(i) for i in read().split()]

# iceberg = []
# melted_ice = []

# # Create and iceberg and melted_iceberg
# for j in range(y):
#     iceberg.append([int(i) for i in read().split()])
#     melted_ice.append([0 for _ in range(x)])


       
# # 빙산이 녹는 과정의 알고리즘
# def melt_ice(iceberg):
#     for j in range(1, y-1):
#         for i in range(1, x-1):
            
#             if iceberg[j][i] == 0:
#                 continue
            
#             for a in range(4):
#                 ny = j + dy[a]
#                 nx = i + dx[a]
                
#                 if iceberg[ny][nx] == 0:
#                     # 이미 여기서 melted_ice의 정보가 담겨 있다.
#                     melted_ice[j][i] += 1
            
            
#     for j in range(1, y-1):
#         for i in range(1, x-1):
#             iceberg[j][i] -= melted_ice[j][i]
#             if iceberg[j][i] < 0:
#                 iceberg[j][i] = 0
#             melted_ice[j][i] = iceberg[j][i]
            

# # dfs로 빙산 개수 카운트
# def dfs(root):
    
#     stack = [root] # (y,x) 좌표를 의미함

#     while(stack):

#         node = stack.pop()
#         melted_ice[node[0]][node[1]] = 0
        
#         for i in range(4):
#             ny = node[0] + dy[i]
#             nx = node[1] + dx[i]
            
#             if (0 <= nx < x) and (0 <= ny < y) and (melted_ice[ny][nx] != 0):
#                 stack.append((ny,nx))



# iterate = 0

# while (1):
    
#     iterate += 1
#     melt_ice(iceberg)
    
#     cnt = 0
#     for j in range(1, y - 1):
#         for i in range(1, x - 1):
#             if melted_ice[j][i] != 0:
#                 dfs((j, i))
#                 cnt += 1
                   
#     if cnt == 0:
#         # print("Completely melted")
#         iterate = 0
#         break
    
#     elif cnt > 1:
#         # print("Splited into {} parts".format(cnt))
#         break
            
# print(iterate)