# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_traversal(self, node, res):
      if node is None:
        return
      
      self.get_traversal(node.left, res)
      res.append(node.val)
      self.get_traversal(node.right, res)
      
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      if root is None:
        return []
      
      # recursive method
      
      # res = []
      # self.get_traversal(root, res)
      # return res
      
      # iterative
      in_order = []
      stack = []
      curr = root
      while True:
        if curr:
          stack.append(curr)
          curr = curr.left
        else:
          if len(stack) == 0:
            break
          curr = stack.pop()
          in_order.append(curr.val)
          curr = curr.right
          
      return in_order