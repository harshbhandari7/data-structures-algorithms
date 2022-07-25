# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_traversal(self, node, postorder):
      if node is None:
        return
      
      self.get_traversal(node.left, postorder)
      self.get_traversal(node.right, postorder)
      postorder.append(node.val)
      
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      if root is None:
        return []
      
      # recursive 
      
      # postorder = []
      # self.get_traversal(root, postorder)
      
      # return postorder
      
      # iterative
      
      postorder = []
      stack = [root]
      
      while stack:
        top = stack.pop()
        if top:
          postorder.append(top.val)
          stack.append(top.left)
          stack.append(top.right)
      
      return postorder[::-1]
    
      
        
        