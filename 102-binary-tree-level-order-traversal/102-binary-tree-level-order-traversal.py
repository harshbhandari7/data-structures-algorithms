# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_node(self, node, nodes_hash, level):
        if node:
            if level not in nodes_hash:
                nodes_hash[level] = []
            nodes_hash[level].append(node.val)
            
            self.get_node(node.left, nodes_hash, level+1)
            self.get_node(node.right, nodes_hash, level+1)
        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        nodes_hash = {}
        self.get_node(root, nodes_hash, 0)
        return [nodes_hash[i] for i in nodes_hash.keys()]
        