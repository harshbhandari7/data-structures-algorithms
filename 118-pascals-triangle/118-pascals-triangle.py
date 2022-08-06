class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = []
        for i in range(numRows):
          tri.append([-1] * (i+1))
        
        tri[0][0] = 1
        for i in range(1, numRows):
          tri[i][0] = tri[i][-1] = 1
          leng = len(tri[i])
          for j in range(1, leng-1):
            tri[i][j] = tri[i-1][j-1] + tri[i-1][j]
          
        return tri
            
            