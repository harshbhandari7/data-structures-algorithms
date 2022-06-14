class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        leng1 = len(word1)
        leng2 = len(word2)
        
        dp = [[1000]*(leng2+1) for i in range(leng1+1)]
	    
        for i in range(leng1 + 1):
            for j in range(leng2 + 1):
                if (i == 0 or j == 0):
                    dp[i][j] = i + j    
                elif (word1[i - 1] == word2[j - 1]):
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
        
        return dp[-1][-1]