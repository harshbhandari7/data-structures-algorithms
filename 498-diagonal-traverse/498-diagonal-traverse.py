from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row = len(mat)
        col = len(mat[0])
        
        diagonal = []
        hash_map = defaultdict(list)
        for i in range(row):
          for j in range(col):
            hash_map[i+j].append(mat[i][j])
        
        for key in hash_map:
          lst = hash_map[key]
          
          if key % 2 == 0:
            lst = lst[::-1]
            
          for ele in lst:
            diagonal.append(ele)
        
        return diagonal
            
            
        