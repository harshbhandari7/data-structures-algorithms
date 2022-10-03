class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
          return matrix
        
        r = len(matrix)
        c = len(matrix[0])
        
        for row in matrix:
          if target in row:
            return True
        
        return False
          
          