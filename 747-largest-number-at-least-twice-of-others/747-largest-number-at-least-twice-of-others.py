class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        leng = len(nums)
        ind = -1
        maxi = float('-inf')
        for i in range(leng):
          if nums[i] > maxi:
            maxi = nums[i]
            ind = i
        
        for i in range(leng):
          if nums[i] != maxi and 2 * nums[i] > maxi:
            return -1
        
        return ind
        
        
          