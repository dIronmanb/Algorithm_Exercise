import sys
read = sys.stdin.readline

def get_parent(parent, x):
    
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    
    if a == b:
        return
    
    if rank[a] < rank[b]:
        parent[a] = b
    else:
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1


test_case = int(read())

for i in range(test_case):
    F = int(read())
    
    case = {}
    rank = {}
    flag = True
    first = None
    
    for j in range(F):
        name1, name2 = [name for name in read().split()]
        cnt = 0
        
        if flag:
            first = name1
            flag = False 
        
        if name1 not in rank.keys():
            rank[name1] = 0

        if name2 not in rank.keys():
            rank[name2] = 0
        
        if name1 not in case.keys():
            case[name1] = name1

        if name2 not in case.keys():
            case[name2] = name2
        
        union_parent(case, name1, name2)
        
        parent = get_parent(case, first)
        
        for key in case.keys():
            
            if parent == get_parent(case, key):
                case[key] = parent
                cnt += 1
        
        # print(case)
        print(cnt)
    
