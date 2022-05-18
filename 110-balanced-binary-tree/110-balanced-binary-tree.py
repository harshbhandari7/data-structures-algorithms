# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse_node(self, node):
        if not node:
            return 0
        
        left  = self.traverse_node(node.left)
        right = self.traverse_node(node.right)
        
        return (max(left, right) + 1)
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        left_h = self.traverse_node(root.left)
        right_h = self.traverse_node(root.right)
           
        return (self.isBalanced(root.left) and self.isBalanced(root.right) and abs(left_h - right_h) <= 1)

        