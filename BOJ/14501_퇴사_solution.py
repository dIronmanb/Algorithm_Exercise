import sys
from collections import deque
read = sys.stdin.readline




leave = int(read())
work_table = deque()
price_table = []
money = 0
impossible = [0] * days


temp = []
process = deque()

for i in range(leave):
    work_table.append([int(i) for i in read().split()])


for i in range(leave):
    days, pay = work_table.popleft()
    next_day = i + days

    if next_day > leave:
        impossible[i] = True
    else:
        temp.append((days, pay))
        for i in range(days, leave):
            if i + work_table[i][0] <= leave:
                process.append(i)
        
        for i in process:
            days, pay = work_table[i]
            next_day = i + days

            if next_day > leave:
                impossible[i] = True
            else:
                temp.append
                