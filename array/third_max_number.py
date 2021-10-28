#Given an integer array nums, return the third distinct maximum number in this array.
#If the third maximum does not exist, return the maximum number.

nums = list(map(int, input().split()))

nums = list(set(nums))
max_e = [float('-inf')] * 3

for ele in nums:
	if ele > max_e[0]:
		max_e = [ele, max_e[0], max_e[1]]
	elif ele > max_e[1]:
		max_e = [max_e[0], ele, max_e[1]]
	elif ele > max_e[2]:
		max_e = [max_e[0], max_e[1], ele]

third_max = max_e[2] if max_e[2] != float('-inf') else max_e[0]
print(third_max)