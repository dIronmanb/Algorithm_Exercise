import math
from collections import deque

def solution(progresses, speeds):
    terms = deque()
    count = 1
    counts = []

    for i in range(len(progresses)):
        terms.append( math.ceil((100 - progresses[i]) / speeds[i]) )
    print(terms)

    # [10, 6, 2, 7, 8, 45, 2, 10]
    release = terms[0]
    for i in range(1,len(terms)):
        if release >= terms[i]:
            count += 1
        else:
            counts.append(count)
            count = 1
            release = terms[i]

    counts.append(count)
    return counts