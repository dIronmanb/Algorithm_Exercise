# -*- coding: utf-8 -*-

from collections import deque

          
def DFS(start_node):
    
    visited = []
    stack = deque()
    stack.append(start_node)
    
    ## 방문이 필요한 리스트가 아직 존재한다면
    while stack:
        node = stack.popleft()

        if len(node[0]) == 1:
            return 1 if node[0] == 1 else 0

        if node[0] <= -1 or node[0] >= width or node[1] <= -1 or node[1] >= height:
            continue

        if node not in visited:

            visited.append(node)
            
            if graph[node[0]][node[1]] == 1:
            ## 인접 노드들을 방문 예정 리스트에 추가
                stack.extend([node[0] + 1, node[1]])
                stack.extend([node[0] - 1, node[1]])
                stack.extend([node[0], node[1] + 1])
                stack.extend([node[0], node[1] - 1])
                stack.extend([node[0] + 1, node[1] + 1])
                stack.extend([node[0] + 1, node[1] - 1])
                stack.extend([node[0] - 1, node[1] + 1])
                stack.extend([node[0] - 1, node[1] - 1])

                
    return visited



result = []
width, height = map(int, input().split()) #맵의 크기는 계산 중에 변하지 X
while (width, height) != (0,0):
    graph = []
    for i in range(height):
        graph.append(list(map(int, input().split())))

    #DFS
    for i in range(width):
        for j in range(height):
            if graph[i][j] == 1:
                val = [i,j]
                break
    result.append(DFS(val))
    width, height = (map(int, input().split()))


for i in range(len(result)):
    print(result[i])