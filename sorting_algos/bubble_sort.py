'''
BUBBLE SORT

- Simplest sorting algo.
- Works by repeatedly swapping the adjacent elements, if they are in wrong order moving to an end.

Complexity:

- Worst/Average case: O(n**2)
-  Best case: O(n)

- Space: O(1)
- Stable
- Inplace

Applications:

- Bubble sort is popular in computer graphics used in polygon filling algo.
- It is capable to detect a very small error (like swap of just 2 elements) in almost sorted
  array and fix with linear complexity.

'''

# ALGORITHM:

nums = list(map(int, input().split()))

def bubble_sort(nums):
	leng = len(nums)
	for i in range(leng-1): # need to iterate 1 less than length
		flag = 0
		for j in range(leng-i-1): # here we iterate till unsorted part.
			if nums[j] > nums[j+1]:
				nums[j], nums[j+1] = nums[j+1], nums[j]
				flag = 1
		if flag == 0:
			break
	return nums

print(bubble_sort(nums))