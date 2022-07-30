from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
          return 0
        
        level = 0
        q = deque()
        
        q.append(root)
        
        while q:
          leng = len(q)
          for i in range(leng):
            node = q.popleft()
            if node.left:
              q.append(node.left)
            if node.right:
              q.append(node.right)
          
          level += 1
        
        return level