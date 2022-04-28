import sys
# combination
from itertools import combinations
read = sys.stdin.readline


dwarfs = []
for i in range(9):
    dwarfs.append(int(read()))
    
two_dwarfs = list(combinations(dwarfs, 2))

for i in range(len(two_dwarfs)):
    seven_drwafs = [j for j in dwarfs if j not in two_dwarfs[i]]
    if sum(seven_drwafs) == 100:
        break
    
seven_drwafs.sort()
for i in seven_drwafs:
    print(i)
    
# print(len(seven_drwafs))