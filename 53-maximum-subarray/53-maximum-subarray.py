class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      leng = len(nums)
      max_sum = curr_sum = nums[0]
      for i in range(1, leng):
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_sum = max(curr_sum, max_sum)
        
      return max_sum
        