class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        leng = len(nums)
        for i in range(leng-1):
          prev = nums[i] + nums[i+1]
          for j in range(i+1, leng-1):
            curr = nums[j] + nums[j+1]
            if prev == curr:
              return True
        
        return False