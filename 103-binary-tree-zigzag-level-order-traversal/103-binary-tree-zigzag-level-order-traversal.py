from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
          return []
        
        order = []
        q = deque()
        q.append(root)
        level = 0
      
        while q:
          lst = []
          for i in range(len(q)):
            node = q.popleft()
            lst.append(node.val)
            
            if node.left:
              q.append(node.left)
            if node.right:
              q.append(node.right)
          
          if level % 2 == 0:
            order.append(lst)
          else:
            order.append(lst[::-1])
          level += 1
            
        return order
              
            
          