class Solution:
    def get_path(self, i, j, grid, memo):
        if i == 0 and j == 0:
          return grid[0][0]
        
        if i < 0 or j < 0:
          return float('inf')
          
        if (i, j) in memo:
          return memo[(i, j)]
        
        up = grid[i][j] + self.get_path(i-1, j, grid, memo)
        left = grid[i][j] + self.get_path(i, j-1, grid, memo)
        mini = min(up, left)
        memo[(i, j)] = mini
        return mini
          
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        m = len(grid)
        n = len(grid[0])
        
        return self.get_path(m-1, n-1, grid, memo)