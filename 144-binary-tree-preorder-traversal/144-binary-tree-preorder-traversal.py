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
      
      # recursive approach
      
      # preorder = []
      # self.get_traversal(root, preorder)
      # return preorder
      
      
      # iterative approach
      
      preorder = []
      curr = root
      stack = []
      
      while True:
        if curr is not None:
          stack.append(curr)
          preorder.append(curr.val)
          curr = curr.left
        else:
          if len(stack) == 0:
            break
          
          curr = stack.pop()
          curr = curr.right
      
      return preorder 
          
          
          
          
      
      
        