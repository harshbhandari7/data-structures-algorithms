'''
MERGE SORT

- A divide and conquer algorithm based on the idea of breaking down a list into several
  sub lists untill each sublists consist of a single element and merging those sublists that
  results into a sorted list.
- Recursive

Complexity:

- Worst/Average case: O(nlogn)

- Space: O(n)
- Stable
- Not-Inplace

'''

# ALGORITHM:

nums = list(map(int, input().split()))

# merge function -> to merge the sorted sub lists
def merge_list(left, right, nums):
  i, j, k = 0, 0, 0
  lengL = len(left)
  lengR = len(right)
  lengNums = len(nums)

  while(i < lengL and j < lengR):
    if (left[i] < right[j]):
      nums[k] = left[i]
      i += 1
    else:
      nums[k] = right[j]
      j += 1
    k += 1

  while(i < lengL):
    nums[k] = left[i]
    i += 1
    k += 1

  while(j < lengR):
    nums[k] = right[j]
    j += 1
    k += 1

# merge sort
def merge_sort(nums):
  leng = len(nums)

  if leng < 2:
    return nums

  mid = leng // 2

  left = nums[:mid]
  right = nums[mid:leng]

  merge_sort(left)
  merge_sort(right)
  # merging the sorted sub lists
  merge_list(left, right, nums)

  return nums

print(merge_sort(nums))