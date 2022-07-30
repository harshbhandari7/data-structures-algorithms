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
      
      return 1 + max(left, right)
      
      
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
      if root is None:
        return True
      
      
      left = self.get_depth(root.left)
      right = self.get_depth(root.right)
      
      return (abs(left-right) < 2) and self.isBalanced(root.left) and self.isBalanced(root.right)