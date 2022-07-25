# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_traversal(self, node, preorder):
      if node is None:
        return
      
      preorder.append(node.val)
      self.get_traversal(node.left, preorder)
      self.get_traversal(node.right, preorder)
      
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      if root is None:
        return []
      
      preorder = []
      self.get_traversal(root, preorder)
      return preorder
        
        