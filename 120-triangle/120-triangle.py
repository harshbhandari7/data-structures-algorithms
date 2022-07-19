class Solution:
    def get_sum(self, i, j, grid, memo):
      if i == len(grid) - 1:
        return grid[i][j]
      
      if (i, j) in memo:
        return memo[(i, j)]
      
      bottom = grid[i][j] + self.get_sum(i+1, j, grid, memo)
      right = grid[i][j] + self.get_sum(i+1, j+1, grid, memo)
      
      curr = min(bottom, right)

      memo[(i, j)] = curr
      return curr
      
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        return self.get_sum(0, 0, triangle, memo)