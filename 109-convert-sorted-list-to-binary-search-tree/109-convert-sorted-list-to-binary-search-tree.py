# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
          return None
        
        if not head.next:
          return TreeNode(head.val)
        
        slow = head
        fast = head.next.next
        while fast and fast.next:
          slow = slow.next
          fast = fast.next.next
        
        curr = slow.next
        slow.next = None
        
        root = TreeNode(curr.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(curr.next)
        
        return root
      
      
        