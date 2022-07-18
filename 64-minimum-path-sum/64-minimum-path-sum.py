class Solution:
    def get_sum(self, i, j, grid, memo):
      if i == 0 and j == 0:
        return grid[i][j]
      
      if i < 0 or j < 0:
        return float('inf')
      
      if (i, j) in memo:
        return memo[(i, j)]
      
      up = grid[i][j] + self.get_sum(i-1, j, grid, memo)
      left = grid [i][j] + self.get_sum(i, j-1, grid, memo)
      mini = min(up, left)
      memo[(i, j)] = mini
      return mini
      
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        r = len(grid)
        c = len(grid[0])
        return self.get_sum(r-1, c-1, grid, memo)