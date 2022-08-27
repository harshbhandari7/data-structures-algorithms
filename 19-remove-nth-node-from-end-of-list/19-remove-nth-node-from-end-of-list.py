# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        leng = 0
        while curr:
          curr = curr.next
          leng += 1
        
        index = leng - n
        
        if index == 0:
          head = head.next
          return head
        
        idx = 0
        curr2 = head
        while idx < index - 1:
          curr2 = curr2.next
          idx += 1
        
        curr2.next = curr2.next.next
        return head