class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = -1
        leng = len(s)
        chars = {}
        
        for i in range(leng):
            if (s[i] in chars):
                chars[s[i]] += 1
            else:
                chars[s[i]] = 1
        
        for i in range(leng):
            if chars[s[i]] == 1: return i
            
        return res