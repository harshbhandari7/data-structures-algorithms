class Solution:
    def get_sum(self, i, j, grid, memo, mini):
      if i == len(grid) - 1:
        return grid[i][j]
      
      if (i, j) in memo:
        return memo[(i, j)]
      
      bottom = self.get_sum(i+1, j, grid, memo, mini)
      right = self.get_sum(i+1, j+1, grid, memo, mini)
      
      curr = grid[i][j] + min(bottom, right)
      print('curr-', curr)
      mini += curr
      memo[(i, j)] = mini
      return mini
      
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        print('sytart')
        return self.get_sum(0, 0, triangle, memo, 0)