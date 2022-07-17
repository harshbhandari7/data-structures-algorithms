class Solution:
    def get_path(self, i, j, dp):
      if i == 0 and j == 0:
        return 1
      
      if i < 0 or j < 0:
        return 0
      
      if (i,j) in dp:
        return dp[(i,j)]
      
      left = self.get_path(i, j-1, dp)
      up = self.get_path(i-1, j, dp)
      
      dp[(i, j)] = left + up
      return left + up
    
    def uniquePaths(self, m: int, n: int) -> int:
      dp = {}
      return self.get_path(m-1, n-1, dp)
        