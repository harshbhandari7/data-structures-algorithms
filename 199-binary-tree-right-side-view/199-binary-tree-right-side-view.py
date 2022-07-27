from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_view(self, node, lst, level):
      if node is None:
        return
      
      if len(lst) == level:
        lst.append(node.val)
      
      self.get_view(node.right, lst, level+1)
      self.get_view(node.left, lst, level+1)
        
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
          return []
        
        # recursive
        res = []
        self.get_view(root, res, 0)
        return res
        
        # iterative
        
#         rview = []
#         q = deque([])
       
#         q.append(root)
        
#         while q:
#           rview.append(q[-1].val)
        
#           leng = len(q)
#           for i in range(leng):    
#             node = q.popleft()
            
#             if node.left:
#               q.append(node.left)
#             if node.right:
#               q.append(node.right)
              
#         return rview
          