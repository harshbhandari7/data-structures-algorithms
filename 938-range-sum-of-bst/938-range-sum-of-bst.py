# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_node_val(self, node, low, high):
        if not node:
            return 0
        
        curr_sum = 0
        
        if node.val >= low and node.val <= high:
            curr_sum += node.val
            
        curr_sum += self.get_node_val(node.left, low, high)
        curr_sum += self.get_node_val(node.right, low, high)
        
        return curr_sum
    
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.get_node_val(root, low, high)
        