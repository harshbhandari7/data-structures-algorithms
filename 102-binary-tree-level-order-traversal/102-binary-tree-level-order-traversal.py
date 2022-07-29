# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_order(self, node, order, level):
      if node:
        if level not in order:
          order[level] = []
        order[level].append(node.val)
        
        self.get_order(node.left, order, level+1)
        self.get_order(node.right, order, level+1)
      
      
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      if root is None:
        return []
      
      order = {}
      curr_level = 0
      self.get_order(root, order, curr_level)
      
      res = []
      for level in order:
        res.append(order[level])
      
      return res
        