class Solution:
    def get_sum(self, ind, nums, dp):
      if dp[ind] != -1:
        return dp[ind]
      
      if ind == 0:
        return nums[ind]
      
      if ind < 0:
        return 0
      
      pick = nums[ind] + self.get_sum(ind-2, nums, dp)
      not_pick = 0 + self.get_sum(ind-1, nums, dp)
      
      dp[ind] = max(pick, not_pick)
      return dp[ind]
      
    def rob(self, nums: List[int]) -> int:
        leng = len(nums) - 1
        dp = [-1] * (leng + 1)
        return self.get_sum(leng, nums, dp)