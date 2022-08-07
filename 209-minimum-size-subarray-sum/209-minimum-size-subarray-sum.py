class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        leng = len(nums)
        start = end = curr = 0
        min_leng = float('inf')
        
        while end < leng:
          curr += nums[end]
          end += 1
        
          while start < end and curr >= target:
            curr -= nums[start]
            start += 1
            min_leng = min(min_leng, end - start + 1)
        
        return 0 if min_leng == float('inf') else min_leng