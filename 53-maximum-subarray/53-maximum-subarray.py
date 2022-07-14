class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    leng = len(nums)
    curr = 0
    max_sum = float('-inf')
    
    for i in range(leng):
      curr = max(nums[i], curr+nums[i])
      max_sum = max(max_sum, curr)
    
    return max_sum