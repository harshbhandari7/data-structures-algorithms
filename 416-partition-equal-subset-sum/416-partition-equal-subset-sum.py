class Solution:
    def get_subset(self, ind, nums, k, memo):
      if ind == 0:
        return nums[ind] == k
      
      if k == 0:
        return True
      
      if (ind, k) in memo:
        return False
      
      not_taken = self.get_subset(ind-1, nums, k, memo)
      taken = False
      if nums[ind] <= k:
        taken = self.get_subset(ind-1, nums, k-nums[ind], memo)
      
      curr = not_taken or taken
      memo[(ind, k)] = curr
      return curr
      
    def canPartition(self, nums: List[int]) -> bool:
      s = sum(nums)
      if s % 2 != 0:  
        return False

      target = s // 2
      memo = {}
      return self.get_subset(len(nums)-1, nums, target, memo)