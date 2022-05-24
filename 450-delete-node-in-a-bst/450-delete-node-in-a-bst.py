# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
            
        if root.val > key:
            root.left = self.deleteNode( root.left, key )
        elif root.val < key:
            root.right = self.deleteNode( root.right, key )
        else:
            if (not root.left) or (not root.right):
                root = root.left if root.left else root.right
            else:
                curr_node = root.right
                while curr_node.left:
                    curr_node = curr_node.left
                    
                root.val = curr_node.val
                root.right = self.deleteNode( root.right, curr_node.val )
    
        return root  