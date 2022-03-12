import sys
read = sys.stdin.readline

num_of_operations = int(read())

a = set()
for i in range(num_of_operations):
    oprs =[i for i in read().split()]
    
    if len(oprs) == 1:
        if oprs[0] == 'all':
            a = {i for i in range(1,21)}
        else:
            a = set()
    else:
        opr, num = oprs[0], int(oprs[1])
        if oprs[0] == 'add':
            a.add(num)
        elif oprs[0] == 'remove':
            a.discard(num)
        elif oprs[0] == 'check':
            if num in a:
                print(1)
            else:
                print(0)    
        elif oprs[0] == 'toggle':
            if num in a:
                a.discard(num)
            else:
                a.add(num)
                
#    print(bin(bits))
    

# for i in result:
#    print(i)