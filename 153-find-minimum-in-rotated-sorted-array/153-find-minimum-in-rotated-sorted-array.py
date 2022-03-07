class Solution:
    def findMin(self, nums: List[int]) -> int:
      while (nums[-1] < nums[0]):
        nums = [nums[-1]] + nums[0:-1]
      
      return nums[0]