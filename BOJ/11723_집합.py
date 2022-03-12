import sys
read = sys.stdin.readline


num_operation = int(read())

a = set()
result = []

for _ in range(num_operation):
    
    input = [i for i in read().split()]
    if len(input) == 2:
         operation, num = input
         num = int(num)
    else:
        operation = input

    if operation == 'add':
        a.add(num)
    
    elif operation == 'remove':
    # remove는 해당 원소가 없으면 error를 raise하므로 주의!
        a.discard(num)
      
    elif operation == 'check':
        if num in a:
            print(1)
            #result.append(1)
        else:
            print(0)
            #result.append(0)
            
        
    elif operation == 'toggle':
        if num in a:
            a.discard(num)
        else:
            a.add(num)
        
    elif operation == 'all':
        a = {i for i in range(1, 21)}

    elif operation == 'empty':
        a = a.clear()

# for i in result:
#     print(i)
