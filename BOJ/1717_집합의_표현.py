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

def find_parent(parent, a, b):
    
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    
    if a == b:
        return 1
    else:
        0
        
n, m = [int(i) for i in read().split()]

# {0}, {1}, {2}, ... {n}
a    = [i for i in range(n + 1)]
rank = [0 for _ in range(n + 1)]

for i in range(m):
    
    oper, node1, node2 = [int(i) for i in read().split()]
    
    # Find set
    if oper:
        if find_parent(a, node1, node2):
            print("YES")
        else:
            print("NO")
    
    # Union set
    else:
        union_parent(a, node1, node2)
        
        