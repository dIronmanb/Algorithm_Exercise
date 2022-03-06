weight = int(input())

# Only 5kg
if weight % 5 == 0:
    print(weight // 5)

# 5kg + 3kg
else:
    i = 3
    flag = False
    while weight not in [4,7]:
        if ((weight - i) % 5 == 0):
            flag = True
            break    
        i += 3

        
    if flag:
        print(((weight - i) // 5) + (i // 3))
    else:
        print(-1)
