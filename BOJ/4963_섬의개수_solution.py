import sys
read = sys.stdin.readline
sys.setrecursionlimit(10000)


def dfs(x : int, y : int)->None:
    dx = [1,1,-1,-1,1,-1,0,0]
    dy = [0,1,0,1,-1,-1,1,-1]

    # remove 1 to 0 for removing land
    graph[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
            dfs(nx, ny)


while True:
    w, h = [int(i) for i in read().split()]
    if w == 0 and h == 0:
        break
    graph = []
    count = 0
    for _ in range(h):
        graph.append([int(i) for i in read().split()])
    for i in range(h):
        for j in range(w):
            # if the position is land,
            if graph[i][j] == 1:
                dfs(i, j)
                count += 1

    print(count)
