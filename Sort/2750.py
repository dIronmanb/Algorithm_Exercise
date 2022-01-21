N = int(input())
nums = []

for i in range(N):
    nums.append(int(input()))


for i in range(0, N-1):
    min = i
    for j in range(i+1, N):
        if(nums[min] > nums[j]):
            min = j
            
    temp = nums[i]
    nums[i] = nums[min]
    nums[min] = temp


for i in nums:
    print(i)












    



    
