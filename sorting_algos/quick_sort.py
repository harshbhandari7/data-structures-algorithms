'''
QUICK SORT

- A divide and conquer strategy based sorting algorithm.
- In this algo, a pivot (a central point) is choosen from the array elements.
- Array is partitioned such that left side of pivot contains all elements that are less 
  than  pivot and right side contains all elements greater than pivot.
- sort function given to us by most of the language libraries are implemenations of quick sort.

Versions of quick sort:

- Always picking the 1st element as pivot.
- Always picking the last element as pivot.
- Picking a random element as pivot.
- Picking median as pivot.

Complexity:

- Worst case: O(n**2)
  (worst case is almost always avoided by using a randomized version quick sort)
- Average case: O(nlogn)

- Space Complexity
  Worst Case: O(n)
  Average Case: O(logn)

- Not Stable
- Inplace

'''

# ALGORITHM:

nums = list(map(int, input().split()))

# partition function
def partition(nums, start, end):
  # picking up the last element as pivot
  pivot = nums[end]
  pIndex = start
  for i in range(start, end):
    if (nums[i] <= pivot):
      nums[i], nums[pIndex] = nums[pIndex], nums[i]
      pIndex += 1

  # swapping the pivot with the element where partion occurs.
  nums[pIndex], nums[end] = nums[end], nums[pIndex]

  return pIndex

# quick sort
def quick_sort(nums, start, end):
  if start < end:
    pIndex = partition(nums, start, end)
    quick_sort(nums, start, pIndex-1)
    quick_sort(nums, pIndex+1, end)

  return nums

print(quick_sort(nums, 0, len(nums)-1))