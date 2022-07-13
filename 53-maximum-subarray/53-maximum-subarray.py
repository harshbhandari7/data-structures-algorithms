class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    leng = len(nums)
    dp = [0] * leng
    for i in range(leng):
      dp[i] = max(dp[i-1]+nums[i], nums[i])
    
    return max(dp)