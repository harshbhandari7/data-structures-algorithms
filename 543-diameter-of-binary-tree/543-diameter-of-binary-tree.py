# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_depth(self, node):
      if node is None:
        return 0
      
      left = self.get_depth(node.left)
      right = self.get_depth(node.right)
      
      curr_path = left + right
      
      if curr_path > self.diameter:
        self.diameter = curr_path
      
      return max(left, right) + 1
      
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
      if root is None:
        return 0
      
      self.diameter = 0
      self.get_depth(root)
      
      return self.diameter
      
      
        
        