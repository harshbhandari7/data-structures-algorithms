class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leng = len(nums)
        left, right = 0, sum(nums)
        for i in range(leng):
          right -= nums[i]
          
          if left == right:
            return i
          
          left += nums[i]
        
        return -1