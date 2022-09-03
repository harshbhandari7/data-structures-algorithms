class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        leng = len(nums)
        s = set()
        for i in range(leng-1):
          t = nums[i] + nums[i+1]
          if t in s:
            return True
          
          s.add(t)
        
        return False