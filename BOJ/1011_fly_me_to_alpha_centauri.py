import sys
import math as m
read = sys.stdin.readline

def f(n):
    # print(n)
    a = n / 2
    i = 0
    while(1):
        # print("current a: {} and i: {}".format(a,i))
        a -= i
        i += 1
        if (a <= 0):
            break
    return i-1

test_case = int(read())
test = []

for i in range(test_case):
    start, end = [int(i) for i in read().split()]
    test.append([start, end])
    

for i in range(test_case):
    start, end = test[i]
    dist = end - start
    
    
    # if  m.trunc(m.sqrt(dist)) < m.sqrt(dist) < m.ceil(m.sqrt(dist)):
    #     pass
    
    # a2 = a * 2
    # if dist <= a * (a + 1):
    #     print(a2)
    # else:
    #     print(a2 + 1)
    
    bottom = m.trunc(m.sqrt(dist))
    top = m.ceil(m.sqrt(dist))
    index = f(dist)
    sum = 0
    for j in range(1, index+1):
        sum += j
    sum *= 2
    
#    print("{} >> distance: {}, bottom: {}, top: {}, index: {}".format(i, dist, bottom, top, index))
        
    # 제곱수면
    if bottom == top:
        print(bottom * 2 - 1)
        
    # 절반까지의 합의 2배 라면:
    elif sum == dist:
        print(index * 2)
    
    # 그 이외의 수라면
    else:
        if top == index:
            print(top * 2 - 1)
        else:
            print(bottom * 2)           
            
#    print()
    