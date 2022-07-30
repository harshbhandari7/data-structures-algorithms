# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_height(self, node):
      if node is None:
        return 0
      
      left = self.get_height(node.left)
      right = self.get_height(node.right)
      
      if left == -1 or right == -1 or abs(left-right) > 1:
        return -1
      
      return 1 + max(left, right)
      
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
      if root is None:
        return True
      
      height = self.get_height(root)
      
      return height != -1 