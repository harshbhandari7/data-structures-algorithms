class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        
        if len_s != len_t:
          return False
        
        freq_s = {}
        freq_t = {}
        
        for ch in s:
          if ch in freq_s:
            freq_s[ch] += 1
          else:
            freq_s[ch] = 1
        
        for ch in t:
          if ch in freq_t:
            freq_t[ch] += 1
          else:
            freq_t[ch] = 1
        
        return freq_s == freq_t