# -*- coding: utf-8 -*-
# sum() 대신에 total_weight 사용 (동적프로그래밍)
from collections import deque
import sys
read = sys.stdin.readline

truck_num, bridge_length, weight = [int(i) for i in read().split()]
truck_weights = deque([int(i) for i in read().split()])

bridge = deque(maxlen = bridge_length)
second = 0

total_weight = 0

while True:
    
    if bridge:
        total_weight -= bridge[0]

    if truck_weights and bridge and truck_weights[0] + total_weight <= weight:
        bridge.append(truck_weights.popleft())
        total_weight += bridge[-1]
    else:
        bridge.append(0)
    second += 1

    if not truck_weights and total_weight == 0:
        break

print(second-1)
print("종료")