# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
          return None
        
        slow = fast = temp = head
        
        while fast and fast.next:
          slow = slow.next
          fast = fast.next.next
        
          if slow == fast:
            while temp != slow:
              temp = temp.next
              slow = slow.next
            
            return temp
          
        return None
            