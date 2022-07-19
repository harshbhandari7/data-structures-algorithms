class Solution:
    def get_sum(self, i, j, grid, memo):
      if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return float('inf')
      
      if i == len(grid) - 1:
        return grid[i][j]
      
      if (i, j) in memo:
        return memo[(i, j)]
      
      ld = self.get_sum(i+1, j-1, grid, memo)
      bot = self.get_sum(i+1, j, grid, memo)
      rd = self.get_sum(i+1, j+1, grid, memo)
      
      curr = grid[i][j] + min(ld, bot, rd)
      memo[(i, j)] = curr
      return curr
    
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
      cols = len(matrix[0])
      memo = {}
      mini = float('inf')
      for col in range(cols):
        path_sum = self.get_sum(0, col, matrix, memo)
        mini = min(path_sum, mini)
      
      return mini