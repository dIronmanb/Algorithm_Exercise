import sys
from collections import deque
read = sys.stdin.readline
sys.setrecursionlimit(10000)






graph = []
visited = []
empty = 0

# input information
m, n = [int(i) for i in read().split()]
for i in range(n):
    graph.append([int(a) for a in read().split()])
    visited.append([0]*m)
    # Sum empty spaces
    empty += graph[i].count(-1)


days = 0
pre_tomatoes = 0
while True:
    present_tomatoes = 0
    for i in range(n):
        for j in range(m):
            # If the tomatoes are ripe at that location,
            if graph[i][j] == 1:
                present_tomatoes += 1
                bfs(i,j)

    print('\n')  
    for i in range(n):
        print(graph[i])

    # If there is no difference in the number of ripe tomatoes from the previous day and today
    if(present_tomatoes == pre_tomatoes):
        break

    # When all the tomatoes have been already ripe
    elif(m * n + empty - present_tomatoes == 0):
        break

    else:
        pre_tomatoes = present_tomatoes
        days += 1

# When all the tomatoes are ripe
if(m * n - empty - present_tomatoes == 0):
      print(days)
# Otherwise
else:
    print(-1)
