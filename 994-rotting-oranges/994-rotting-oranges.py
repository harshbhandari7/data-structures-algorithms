from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        
        fresh = 0
        rotten_list = deque()
        
        for i in range(row):
          for j in range(col):
            if grid[i][j] == 1:
              fresh += 1
            elif grid[i][j] == 2:
              rotten_list.append((i, j))
        
        
        mins = 0
        
        while rotten_list and fresh > 0:
          mins += 1
          for _ in range(len(rotten_list)):
            r, c = rotten_list.popleft()
            
            adjacents = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for i, j in adjacents:
              ar = r + i
              ac = c + j
              
              if ar < 0 or ar == row or ac < 0 or ac == col:
                continue
              if grid[ar][ac] == 0 or grid[ar][ac] == 2:
                continue
              
              fresh -= 1
              grid[ar][ac] = 2
              
              rotten_list.append((ar, ac))
              
        return mins if fresh == 0 else -1