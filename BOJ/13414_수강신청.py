import sys
from collections import defaultdict, OrderedDict
read = sys.stdin.readline


A, I = [int(i) for i in read().split()]
seq = OrderedDict()

for i in range(I):
    num_str = read().rstrip()
    if num_str in seq:
        seq.move_to_end(num_str, last = True)
    else:
        seq[num_str] = 1
       
print(seq)

for i in list(seq.keys())[:A]:
    print(i)
    