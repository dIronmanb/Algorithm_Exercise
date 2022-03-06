import sys
from collections import deque
from itertools import combinations
import copy

read = sys.stdin.readline

di = [1, -1,  0,  0]
dj = [0,  0,  1, -1]

def BFS(j: int, i: int)->None:
     
    for a in range(4):
        ni = i + di[a]
        nj = j + dj[a]
        
        if 0 <= ni < x and 0 <= nj < y and temp_lab[nj][ni] == 0:
            temp_lab[nj][ni] = 2
            BFS(nj, ni)   



y, x = [int(i) for i in read().split()]
lab = []
comb = []
safe_zone = []

for j in range(y):
    lab.append([int(i) for i in read().split()])
    
    
for j in range(y):
    for i in range(x):
        if lab[j][i] == 0:
            comb.append([j,i])
            

comb = list(combinations(comb, 3)) 


a = 0
for walls in comb:
    temp_lab = copy.deepcopy(lab)
    
    cnt = 0
    
    for wall in walls:
        temp_lab[wall[0]][wall[1]] = 1
    
    # BFS
    for j in range(y):
        for i in range(x):
            if temp_lab[j][i] == 2:
                BFS(j,i)
     
    for j in range(y):
        for i in range(x):
            if temp_lab[j][i] == 0:
                cnt += 1 
    
    safe_zone.append(cnt)
    
print(max(safe_zone))

    
    
