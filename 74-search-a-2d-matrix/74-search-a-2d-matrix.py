class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        start, end = 0, (rows * cols) - 1
        
        while start <= end:
          mid = (start + end) // 2
          ele = matrix[mid // cols][mid % cols]
          if target == ele:
            return True
          elif ele < target:
            start = mid + 1
          else:
            end = mid - 1
        
        return False