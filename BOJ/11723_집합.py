import sys
read = sys.stdin.readline

num_of_operations = int(read())

bits = 0b000000000000000000000
# result = []
for i in range(num_of_operations):
    oprs =[i for i in read().split()]
    
    if len(oprs) == 1:
        if oprs[0] == 'all':
            bits = 0b111111111111111111111
        elif oprs[0] == 'empty':
            bits = 0b00000000000000000000
    elif len(oprs) == 2:
        operand = int(oprs[1])
        if oprs[0] == 'add':
            bits |= 1 << operand - 1
        elif oprs[0] == 'remove':
            bits &= 0 << operand - 1
        elif oprs[0] == 'check':
            if bits & (1 << operand - 1) != 0:
                # result.append(1)
                print(1)
            else:
                # result.append(0)
                print(0)    
        elif oprs[0] == 'toggle':
            if bits & (1 << operand - 1) != 0:
                bits &= 0 << int(oprs[1])
            else:
                bits |= 1 << int(oprs[1])
    
#    print(bin(bits))
    

# for i in result:
#    print(i)