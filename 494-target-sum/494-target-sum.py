class Solution:
    def get_exp(self, ind, nums, target, memo):
      if ind == 0:
        if nums[ind] == 0 and target == 0:
          return 2
        
        if nums[ind] == target or target == 0:
          return 1
        
        return 0
      
      if (ind, target) in memo:
        return memo[(ind, target)]
        
      not_take = self.get_exp(ind-1, nums, target, memo)
      take = 0
      if nums[ind] <= target:
        take = self.get_exp(ind-1, nums, target-nums[ind], memo)
      
      summ = take + not_take
      memo[(ind, target)] = summ
      return summ
  
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        leng = len(nums)
        memo = {}
        
        total_sum = sum(nums)
        
        if total_sum - target < 0:
          return 0
        
        if (total_sum - target) % 2 == 1:
          return 0
        
        new_target = (total_sum - target) // 2
        
        return self.get_exp(leng-1, nums, new_target, memo)