from collections import deque

bridge_length = 100
weight = 100
truck_weights = deque([10,10,10,10,10,10,10,10,10,10])


bridge = deque(maxlen = bridge_length)
second = 0
# bridge[  <  <  <  ] 
# 다리를 모두 통과해야 함!

while True:

    if truck_weights and bridge and truck_weights[0] + sum(bridge, start = -bridge[0]) <= weight:
        bridge.append(truck_weights.popleft())
    else:
        bridge.append(0)
    second += 1

    if(not truck_weights) and (sum(bridge) == 0):
        break

    print("다리 상황: {} / 트럭 대기줄: {} / 걸린 시간: {}".format(
                bridge, truck_weights, second 
    ))

print(second)
print("종료")