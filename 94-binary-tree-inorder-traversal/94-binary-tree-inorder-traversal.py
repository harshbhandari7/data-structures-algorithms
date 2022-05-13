# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_node(self, node, nodes_list):
        if node:
            self.get_node(node.left, nodes_list)
            nodes_list.append(node.val)
            self.get_node(node.right, nodes_list)
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        nodes_list = []
        self.get_node(root, nodes_list)
        return nodes_list