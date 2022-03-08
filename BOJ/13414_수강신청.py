import sys
from collections import OrderedDict
read = sys.stdin.readline


A, I = [int(i) for i in read().split()]
seq = OrderedDict()

for i in range(I):
    num = read().rstrip()
    if num in seq:
        seq.move_to_end(num, last = True)
    else:
        seq[num] = 1
       
for i in list(seq.keys())[:A]:
    print(i)
    