# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            idx = inorder.index(preorder.pop(0))
            root_node = TreeNode(inorder[idx])
            
            # left sub-tree
            root_node.left = self.buildTree(preorder, inorder[:idx])
            
            # right sub-tree
            root_node.right = self.buildTree(preorder, inorder[idx+1:])
            
            return root_node