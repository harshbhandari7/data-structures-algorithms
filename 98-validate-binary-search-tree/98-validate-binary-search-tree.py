# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def validate(self, node, low, high):
      if not node:
        return True
      
      if node.val <= low or node.val >= high:
        return False
      
      left_sub_tree = self.validate(node.left, low, node.val)
      right_sub_tree = self.validate(node.right, node.val, high)
      
      return left_sub_tree and right_sub_tree
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        low = float('-inf')
        high = float('inf')
        
        return self.validate(root, low, high)