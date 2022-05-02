# DFS
# union set으로도 풀 수 있다.
import sys
read = sys.stdin.readline

vertex = int(read())

computers = {i : [] for i in range(1, vertex + 1)}
visited = {i:False for i in range(1, vertex + 1)}
edge = int(read())
cnt = 0

for i in range(edge):
    node1, node2 = [int(i) for i in read().split()]
    computers[node1].append(node2)
    computers[node2].append(node1)
    
    
def dfs(computers, x):
    global cnt
    if visited[x] == False:
        visited[x] = True
        cnt += 1
        
        for i in computers[x]:
            dfs(computers, i)


dfs(computers, 1)
print(cnt - 1)