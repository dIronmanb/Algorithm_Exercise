# -*- coding: utf-8 -*-

def dfs(x,y): # 재귀호출에 의한 문제점 발생
    if x <= -1 or x >= width or y <= -1 or y >= height:
        return False
    
    if graph[x][y] == 1:
        #상하좌우 조사
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y - 1)

        #대각 성분도 조사
        dfs(x + 1, y + 1)
        dfs(x + 1, y - 1)
        dfs(x - 1, y + 1)
        dfs(x - 1, y - 1)
        return True
    return False
             


result = []
width, height = map(int, input().split()) #맵의 크기는 계산 중에 변하지 X
while (width, height) != (0,0):
    graph = []
    for i in range(height):
        graph.append(list(map(int, input().split())))

    # DFS
    islands = 0
    for i in range(width):
        for j in range(height):
            if dfs(i, j) == True:
                islands += 1
    
    result.append(islands)
    width, height = (map(int, input().split()))


for i in range(len(result)):
    print(result[i])