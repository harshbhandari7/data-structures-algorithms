class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
      ctr = max_ctr = 0
      leng = len(nums)
      for i in range(leng):
        if nums[i] == 1:
          ctr += 1
        else:
          max_ctr = max(ctr, max_ctr)
          ctr = 0
      
      return max(ctr, max_ctr) 
        