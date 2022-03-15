import sys
read  = sys.stdin.readline


y, x  = [int(i) for i in read().split()]
map_info = []
visited = [[0 for _ in range(x)] for _ in range(y)]
red , blue, hole = None, None, None
result = None
count = 0

for j in range(y):
    line_info = [i for i in read().rstrip()]
    map_info.append(line_info)
        
    for i in range(len(line_info)):
        if 'R' == line_info[i]:
            red = [j,i]
        elif 'B' == line_info[i]:
            blue = [j,i]
        elif 'O' == line_info[i]:
            hole = [j,i]
        

# 상하좌우
dy = [1, -1,  0,  0]
dx = [0,  0, -1,  1]



def dfs(red_y, red_x, blue_y, blue_x):
    
    # 한 번만 진행했을 시 나오는 코드    
    global count 
    global result

    if result is not None:
        return
    

    for i in range(4):
        red_ny = red_y + dy[i]
        red_nx = red_x + dx[i]
        blue_ny = blue_y + dy[i]
        blue_nx = blue_x + dx[i]
        
        if(0 <= red_ny < y and 0 <= red_nx < x and
        0 <= blue_ny < y and 0 <= blue_nx < x):
            empty_way = False
            # if(map_info[red_ny][red_nx] != '#' and
            #    map_info[blue_ny][blue_nx] != '#'):
            
            # 한 번 기울이게 함.
            while((map_info[red_ny][red_nx] != '#' or map_info[blue_ny][blue_nx] != '#')
                  and(visited[red_ny][red_nx] == 0)):
                red_dy, red_dx, blue_dy, blue_dx  = dy[i], dx[i], dy[i], dx[i]
                empty_way = True
                # 파란 공이 들어갔다면, 또는 둘 다 들어갔다면
                if map_info[blue_ny][blue_nx] == 'O':
                    result = -1
                    break
                
                # 빨간 공만 들어가면
                if map_info[red_ny][red_nx] == 'O':
                    result = count
                    
                # count가 10이상이면
                if count >= 10:
                    result = -1
                    break
                        
                
                if map_info[red_ny][red_nx] == '#':
                    red_dy = 0
                    red_dx = 0 
                     
                if map_info[blue_ny][blue_nx] == '#':
                    blue_dy = 0
                    blue_dx = 0
                
                visited[red_ny][red_nx] = 1
                red_ny += red_dy
                red_nx += red_dx
                blue_ny += blue_dy
                blue_nx += blue_dx
                
                print("while map_info")    
                for j in range(y):
                    print(map_info[j])
                print()
                
            
            # 현재 result에 어떤 값이 담겨져 있다는 의미이므로
            if result is not None:
                return
            
            # 현재 #에 닿았으므로 빨간 공, 파란 공의 ny,nx에 -1해주기
            red_ny -= dy[i]
            red_nx -= dx[i]
            blue_ny-= dy[i]
            blue_nx-= dx[i]
            
                    
            # R,B와 남은 여공간을 서로 switch
            map_info[red_y][red_x], map_info[red_ny][red_nx] = map_info[red_ny][red_nx], map_info[red_y][red_x]
            map_info[blue_y][blue_x], map_info[blue_ny][blue_nx] = map_info[blue_ny][blue_nx], map_info[blue_y][blue_x] 
    
            print("between map_info")    
            for j in range(y):
                print(map_info[j])
            print()
            # 좌표값 갱신
            red[0], red[1] = red_ny, red_nx
            blue[0], blue[1]  = blue_ny, blue_nx
            
            count += 1

            # 벽에 둘러싸져 있고 주변이 방문한 곳이라면
            if empty_way == False:
                
                # 이전 값으로 되돌리기
                while (map_info[red_ny][red_nx] != '#' or map_info[blue_ny][blue_nx] != '#'):
                    
                    blue_dy, blue_dx = dy[i], dx[i]
                    red_dy, red_dx = dy[i], dx[i]
                        
                    if map_info[red_ny][red_nx] == '#':
                        red_dy = 0
                        red_dx = 0 
                    if map_info[blue_ny][blue_nx] == '#':
                        blue_dy = 0
                        blue_dx = 0
                    
                    red_ny -= red_dy
                    red_nx -= red_dx
                    blue_ny-= blue_dy
                    blue_nx-= blue_dx
                            
                # 되돌아왔다면 그곳은 1로 설정 -> 세 갈래 길은 존재 X
                if visited[red_ny][red_nx] == True:
                    result = -1
                    break
                else:    
                    visited[red_ny][red_nx] = 1    
                    # R,B와 남은 여공간을 서로 switch
                    map_info[red_y][red_x], map_info[red_ny][red_nx] = map_info[red_ny][red_nx], map_info[red_y][red_x]
                    map_info[blue_y][blue_x], map_info[blue_ny][blue_nx] = map_info[blue_ny][blue_nx], map_info[blue_y][blue_x] 
            
                    # 좌표값 갱신
                    red[0], red[1] = red_ny, red_nx
                    blue[0], blue[1]  = blue_ny, blue_nx
                
                    # count 감소
                    count -= 1
                    
            for j in range(y):
                print(map_info[j])
            print()
                    
            dfs(red[0], red[1], blue[0], blue[1])
                
                
                
dfs(red[0], red[1], blue[0], blue[1])

for j in range(y):
    print(map_info[j])
    
print(result)

# print(map_info)
# print(red, blue, hole)
    