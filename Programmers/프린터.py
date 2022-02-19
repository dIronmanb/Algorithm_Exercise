from collections import deque
def solution(priorities, location):
    priorities = deque(priorities)
    printer = []
    a = deque()
    names = deque([[name, priority] for name, priority in enumerate(priorities)])

    while priorities:
        maximum = max(priorities)
        val = priorities.popleft()
        val_2 = names.popleft()

        if val == maximum:
            printer.append(val_2)
        else:
            priorities.append(val)
            names.append(val_2)
   
    for i in range(len(printer)):
        if location == printer[i][0]:
            return i + 1


# def solution(priorities, location):
#     queue =  [(i,p) for i,p in enumerate(priorities)]
#     answer = 0
#     while True:
#         cur = queue.pop(0) # O(n)
#         if any(cur[1] < q[1] for q in queue):
#             queue.append(cur)
#         else:
#             answer += 1
#             if cur[0] == location:
#                 return answer