'''
SELECTION SORT

- In this algorithm, we find the minimum or maximum in an array depending on the order we want to
  sort it in and then putting it in it's correct position.

- Works by repeatedly finding minimum element(considering sort order to be in ascending) from the
  unsorted part and putting it at the begining.

Complexity:

- Worst/Average case: O(n**2)

- Space: O(1)
- Unstable
- Inplace

'''

# ALGORITHM:
nums = list(map(int, input().split()))

def selection_sort(nums):
	leng = len(nums)
	for i in range(leng-1):
		for j in range(i+1, leng):
			if (nums[i] > nums[j]):
				nums[i], nums[j] = nums[j], nums[i]

	return nums

print(selection_sort(nums))