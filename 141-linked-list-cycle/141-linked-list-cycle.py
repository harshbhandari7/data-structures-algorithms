# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        memo = {}
        curr = head
        while curr:
          if curr in memo:
            return True
          
          memo[curr] = 1
          curr = curr.next
          
        return False