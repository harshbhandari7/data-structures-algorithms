# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
          return None
        
        slow = fast = cycle_start = head
        
        while fast.next and fast.next.next:
          slow = slow.next
          fast = fast.next.next
          
          if slow == fast:
            while slow != cycle_start:
              slow = slow.next
              cycle_start = cycle_start.next
            
            return cycle_start
        
        return None
              