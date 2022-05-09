import sys
read = sys.stdin.readline


test_case = int(read())


for _ in range(test_case):
        
    Map = []
    flag = True
    conveniences = int(read())
    beer = 20.0
    meter_per_beer = 1 / 50.0
     
    for _ in range(conveniences + 2):
        Map.append([int(i) for i in read().split()])
    
    for i in range(1, conveniences + 2):
        x1 , y1  = Map[i]
        x0,  y0  = Map[i-1]
        
        sum = float(abs(x1 - x0) + abs(y1 - y0))
        # drunk_beer = sum * meter_perwjdgmld_beer
        
        beer -= drunk_beer
        
        if beer < 0:
            flag = False
            break
        
        if float(beer) - int(beer) == 0.0:
            beer = 20.0
        else:
            temp = float(beer) - int(beer) # 잔여 양
            beer = 19 + temp      
        
    print("happy" if flag else "sad")
        
        
        
        
        