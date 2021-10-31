nums = list(map(int, input().split()))
k = int(input())
leng = len(nums)

for i in range(k):
	for j in range(leng-1, 0, -1):
		nums[j], nums[j-1] = nums[j-1], nums[j]


print(nums)