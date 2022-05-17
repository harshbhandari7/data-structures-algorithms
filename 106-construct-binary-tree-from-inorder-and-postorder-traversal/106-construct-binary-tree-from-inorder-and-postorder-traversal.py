# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_subtree(self, left, right, val_hash, postorder):
        if left > right:
            return None
        else:
            root = TreeNode(postorder.pop())
            
            mid = val_hash[root.val]
            
            root.right = self.get_subtree( mid+1, right, val_hash, postorder)
            root.left = self.get_subtree( left, mid-1, val_hash, postorder)
            
            return root
        
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        val_hash = { val:index for index, val in enumerate(inorder) }
        
        return self.get_subtree(0, len(inorder)-1, val_hash, postorder)