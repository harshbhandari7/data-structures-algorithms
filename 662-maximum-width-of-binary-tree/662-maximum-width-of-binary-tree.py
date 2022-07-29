from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
      q = deque()
      q.append((root, 0))
      
      width = 0
      
      while q:
        leng = len(q)
        indexes = []
        
        for i in range(leng):
          node, idx = q.popleft()
          indexes.append(idx)
          
          
          if node.left:
            q.append((node.left, 2*idx + 1))
          
          if node.right:
            q.append((node.right, 2*idx + 2))
      
      
        width = max(width, indexes[-1] - indexes[0] + 1)
        
      return width
          
          
      
        
        
        
        
        
        
        
        
        
        
        
        
        
        