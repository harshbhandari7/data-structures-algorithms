from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
          return []
        
        level_order = []
        queue = deque()
        curr_level = 0
        
        queue.append(root)
        
        while queue:
          level_order.append([])
          
          for i in range(len(queue)):
            node = queue.popleft()
            
            level_order[curr_level].append(node.val)
            if node.left:
              queue.append(node.left)

            if node.right:
              queue.append(node.right)
          
          curr_level += 1
        
        return level_order