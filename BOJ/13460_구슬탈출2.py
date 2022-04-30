import sys
read = sys.stdin.readline

vertical, horizon = [int(i) for i in read().split()]
plane = [[] for _ in range(vertical)]

for j in range(vertical):
    plane[j].extend([int(i) for i in read().split()])



    
