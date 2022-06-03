class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        self.integral_image = [ [ 0 for c in range(cols)] for r in range(rows)]
        
        for r in range(rows):
            summ = 0
            for c in range(cols):
                summ += matrix[r][c]
                
                self.integral_image[r][c] = summ
                
                if r > 0:
                    self.integral_image[r][c] += self.integral_image[r-1][c]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottom_right = self.integral_image[row2][col2]
        bottom_left = self.integral_image[row2][col1-1] if col1 >= 1 else 0
        top_right = self.integral_image[row1-1][col2] if row1 >= 1 else 0
        top_left = self.integral_image[row1-1][col1-1] if row1 >= 1 and col1 >= 1 else 0 
        
        summ = bottom_right - top_right - bottom_left + top_left 
        return summ
        
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)