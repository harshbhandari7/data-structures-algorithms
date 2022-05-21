# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_height(self, node):
        if not node:
            return 0
        
        left_h = self.get_height(node.left)
        right_h = self.get_height(node.right)
        
        return 1 + max(left_h, right_h)
    
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_h = self.get_height(root.left)
        right_h = self.get_height(root.right)
        
        dia_root = left_h + right_h
        dia_left = self.diameterOfBinaryTree(root.left)
        dia_right = self.diameterOfBinaryTree(root.right)
        
        dia = max(dia_root, dia_left, dia_right)

        return dia
        