# sum() 대신에 total_weight 사용 (동적프로그래밍)
from collections import deque

bridge_length = 100
weight = 100
truck_weights = deque([10,10,10,10,10,10,10,10,10,10])


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

print(second)
print("종료")