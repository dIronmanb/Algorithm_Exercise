N = int(input()) # 사실상, 수를 정하지 않아도 nums를 받아오면서 해결된다.
nums = list(map(int, input().split()))


for i in range(N-1):
    min = i
    for j in range(i+1, N):
        if(nums[min] > nums[j]):
            min = j
        
    temp = nums[min]
    nums[min] = nums[i]
    nums[i] = temp

# 정렬 이후,
sum = 0

for i in range(N):
    sum += nums[i] * (N - i)    

print(nums)
print(sum)