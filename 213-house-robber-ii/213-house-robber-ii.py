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
    leng = len(nums)
    
    if leng == 1:
      return nums[0]
    
    if leng == 2:
      return max(nums[0], nums[1])
    
    dp = [-1] * (leng-1)
    dp1 = [-1] * (leng-1)

    first_n = nums[:leng-1]
    last_n = nums[1:leng]
    
    self.get_sum(len(first_n)-1, first_n, dp)
    self.get_sum(len(last_n)-1, last_n, dp1)

    return max(dp[-1], dp1[-1])