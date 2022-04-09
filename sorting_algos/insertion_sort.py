'''
INSERTION SORT

- Better than bubble and selection sort. 
- Works by comparing and inserting the element at it's suitable index. 

Complexity:

- Worst/Average case: O(n**2)

- Space: O(1)
- Stable
- Inplace

'''

# ALGORITHM:

nums = list(map(int, input().split()))

def insertion_sort(nums):
  leng = len(nums)
  for i in range(1, leng):
    value = nums[i]
    hole = i
    while(hole > 0 and nums[hole-1] > value):
      nums[hole] = nums[hole-1]
      hole -= 1
    nums[hole] = value 
  
  return nums

print(insertion_sort(nums))