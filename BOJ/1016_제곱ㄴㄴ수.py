import sys
read = sys.stdin.readline
from timeit import default_timer as timer

Min, Max = [int(i) for i in read().split()]

nums = {i : False for i in range(Min, Max +1)}
diff = Max - Min + 1
i = 2


start = timer()

while i ** 2 <= Max:
    
    # Get the quote of Min
    q = Min // i**2
    
    # if quote is not zero, (Now there is reminder)
    # add 1 from the quotient to exsit within the range: q * (i ** 2) > Min
    if Min % i**2 != 0:
        q += 1
    
    # q * (i ** 2) corresponds to "제곱수"
    while q * i ** 2<= Max:
        
        if nums[q * i ** 2] == False:
            nums[q * i ** 2] = True
            diff -= 1
        
        q += 1
    
    i += 1
    
print(diff)    
print(timer() - start)  
    
        
    