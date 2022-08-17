class Solution:
    def romanToInt(self, s: str) -> int:
        leng = len(s)
        nums = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
        n = i = 0
        while i < leng - 1:
          if nums[s[i]] < nums[s[i+1]]:
            n += nums[s[i+1]] - nums[s[i]]
            i += 2
          else:
            n += nums[s[i]]
            i += 1
        
        if i == leng - 1:
          n += nums[s[i]]
        
        return n