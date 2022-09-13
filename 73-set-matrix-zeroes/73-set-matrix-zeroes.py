class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        
        row_zeroes = [0] * r
        col_zeroes = [0] * c
        
        for i in range(r):
          for j in range(c):
            if matrix[i][j] == 0:
              row_zeroes[i] = col_zeroes[j] = 1
        
        for i in range(r):
          for j in range(c):
            if row_zeroes[i] or col_zeroes[j]:
              matrix[i][j] = 0
          
          
            
        
          