nums = list(map(int, input().split()))
target = int(input())

def two_sum(nums):
	leng = len(nums)
	diff_dict = {}
	for i in range(leng):
		diff = target - nums[i]
		if diff in diff_dict:
			return [diff_dict[diff], i]
		diff_dict[nums[i]] = i
	return -1

print(two_sum(nums))