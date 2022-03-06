class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        beg, end = 0, (rows * cols) - 1
        while(beg <= end):
            mid = (beg + end) // 2
            num = matrix[mid // cols ][mid % cols]
            if (target == num):
                return True
            elif (num < target):
                beg = mid + 1
            else:
                end = mid - 1
        return False