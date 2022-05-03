from collections import deque
# from timeit import default_timer as timer
import sys
read = sys.stdin.readline


# N은 학생 수, M은 비교한 횟수
n, m = [int(i) for i in read().split()]

graph = {i: [] for i in range(1, n + 1)}
visited = {i : False for i in range(1, n + 1)}
sequence = deque()

for i in range(m):
    first, second = [int(i) for i in read().split()]
    graph[first].append(second)
    
    
# # DFS
def dfs(graph, node):
    visited[node] = True
    
    for i in graph[node]:
        if visited[i] == False:
            dfs(graph, i)

    sequence.appendleft(node)
               

# start = timer()

for nodes in graph.values():
    
    for node in nodes:
        if visited[node] == False:
            dfs(graph, node)
    
for key in graph.keys():
    
    if visited[key] == False:
        visited[key] = True
        sequence.appendleft(key)
    
for i in sequence:
    print(i, end = " ")
    
# print(timer() - start)