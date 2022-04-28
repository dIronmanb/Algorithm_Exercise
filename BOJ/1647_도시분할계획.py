import sys
read = sys.stdin.readline

def get_parent(parent, x):
    
    # single node with no connection 
    if parent[x] == x:
        return x
    # otherwise, call my parent node recursively
    parent[x] = get_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    
    # connect smaller ones
    if a < b:
        parent[b] = a
    else:
        parent[a] = b    

def find_parent(parent, a, b):

    a = get_parent(parent, a)
    b = get_parent(parent, b)
    
    if a == b:
        return 1
    else:
        return 0   
    
# definite edge class 
class Edge():
    
    def __init__(self, a, b, cost):
        self.node = [a,b]
        self.cost = cost
        
# make empty list called "road"
road = []

# definite number of houses and road
house_num, road_num = [int(i) for i in read().split()]

# Create edge info between two houses
for _ in range(road_num):
    a, b, cost = [int(i) for i in read().split()]
    road.append(Edge(a, b, cost))

# sort by cost of edge
road.sort(key = lambda x : x.cost)

# save where the graph contains eac  h node
parent =  [0] * (house_num + 1)
for i in range(1, house_num + 1):
    parent[i] = i
    

sum = 0         # total maintenance
edge_num = 0    # edge num = vertex - 1
last_index = 0       # to determine the index immediately before connecting to the last node

for i in range(len(road)):
    
    last_index += 1
    # if there is no cycle
    if not find_parent(parent, road[i].node[0], road[i].node[1]):
        sum += road[i].cost
        edge_num += 1        
        union_parent(parent, road[i].node[0], road[i].node[1])

    if edge_num == house_num - 1:
        break
    

print(sum)
print(sum - road[last_index - 1].cost)
    
    

                    
    
    