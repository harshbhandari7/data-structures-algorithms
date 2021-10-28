#Given an integer array nums, return the second distinct maximum number in this array.

nums = list(map(int, input().split()))

nums = list(set(nums))
max_e = [float('-inf')] * 2

for ele in nums:
	if ele > max_e[0]:
		max_e = [ele, max_e[0]]
	elif ele > max_e[1]:
		max_e = [max_e[0], ele]

second_max = max_e[1] if max_e[1] != float('-inf') else max_e[0]
print(second_max)