class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        leng = len(grid)
        for i in range(leng):
            for j in range(leng):
                if i == j or i+j == leng - 1:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j]:
                        return False

        return True
                    