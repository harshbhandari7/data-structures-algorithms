class Solution:
    def get_seq(self, ind1, ind2, text1, text2, memo):
      if ind1 < 0 or ind2 < 0:
        return 0
      
      if (ind1, ind2) in memo:
        return memo[(ind1, ind2)]
      
      if text1[ind1] == text2[ind2]:
        return 1 + self.get_seq(ind1-1, ind2-1, text1, text2, memo)
      
      maxi = max(
        self.get_seq(ind1-1, ind2, text1, text2, memo),
        self.get_seq(ind1, ind2-1, text1, text2, memo)
      )
      
      memo[(ind1, ind2)] = maxi
      return maxi
      
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        leng1 = len(text1)
        leng2 = len(text2)
        
        memo = {}
        
        return self.get_seq(leng1-1, leng2-1, text1, text2, memo)
        