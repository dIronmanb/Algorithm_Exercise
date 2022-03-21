wanted_length = int(input())



sticks = []
sticks.append(64)


while sum(sticks) != wanted_length:
    stick = sticks.pop()
    half_stick = stick//2
    sticks.append(half_stick)
    
    
    if sum(sticks) >= wanted_length:
#        print(sticks)
        pass
    else:
        sticks.append(half_stick)
#        print(sticks)
               
                  
#print(sticks)
print(len(sticks))