import sys
read = sys.stdin.readline

def get_parent(graph, a):
    if graph[a] == a:
        return a
    graph[a] = get_parent(graph, graph[a])
    return graph[a]

def union_parent(graph, a, b):
    a_parent = get_parent(graph, a)
    b_parent = get_parent(graph, b)
    
    if a_parent > b_parent:
        graph[a_parent] = b_parent
    else:
        graph[b_parent] = a_parent
        
def find_parent(graph, a, b):
    if(get_parent(graph, a) == get_parent(graph, b)):
        return 1
    else:
        return 0
  
city_num = int(read())
city_wanted_num = int(read())
cities = [[] for _ in range(city_num)]

graph = [i for i in range(city_num)]

for j in range(city_num):
        cities[j].extend([int(i) for i in read().split()])
        
        
for j in range(city_num):
    # [0, 1, 1, 1, 1 ...]
    for i in range(city_num):
        # If the city is connected,
        if cities[j][i]:
            union_parent(graph, i, j)
            
city_list = []        
city_list.extend([int(i) - 1 for i in read().split()])
    
    
flag = True      
for i in range(1, len(city_list)):
    if not find_parent(graph, city_list[i-1], city_list[i]):
        flag = False
        break
        
        
if flag:
    print("YES")
else:
    print("NO")