class Solution:
    def get_path(self, i, j, grid, dp):
      if grid[i][j] == 1:
        return 0
      
      if i == 0  and j == 0:
        return 1
      
      if i < 0 or j < 0:
        return 0
      
      if (i, j) in dp:
        return dp[(i, j)]
      
      up = self.get_path(i-1, j, grid, dp)
      left = self.get_path(i, j-1, grid, dp)
      
      dp[(i, j)] = up + left
      
      return up + left
      
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = {}
        r = len(obstacleGrid)
        c = len(obstacleGrid[0])
        
        return self.get_path(r-1, c-1, obstacleGrid, dp)