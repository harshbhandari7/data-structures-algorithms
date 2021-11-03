'''
Given an integer array nums,find the contiguous subarray
(containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.
'''

# check kadane's algo!

def max_of_subarray(nums):
	max_sum = float('-inf')
	current_sum = 0

	for ele in nums:
		current_sum += ele
		if (current_sum > max_sum):
			max_sum = current_sum
		if (current_sum < 0):
			current_sum = 0

	return max_sum 


nums = list(map(int, input().split()))
print(max_of_subarray(nums))
