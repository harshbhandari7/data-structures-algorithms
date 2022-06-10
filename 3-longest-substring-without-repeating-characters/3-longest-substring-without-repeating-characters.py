class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        leng = len(s)
        if leng == 0 or leng == 1:
            return leng
    
        start = 0
        maxi = 0
        char_hash = {}
        
        for i in range(leng):
            if s[i] in char_hash and start <= char_hash[s[i]]:
                start = char_hash[s[i]] + 1
            else:
                maxi = max(maxi, i - start + 1)
            
            char_hash[s[i]] = i
            
        return maxi
                
            