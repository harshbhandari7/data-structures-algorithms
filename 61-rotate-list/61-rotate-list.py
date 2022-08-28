# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
          return head
        
        leng = 0
        temp = head
        while temp:
          temp = temp.next
          leng += 1
        
        k = k % leng
        
        while k > 0:
          
          i = 1
          dumm = curr = head
          while i < leng - 1:
            curr = curr.next
            i += 1
          
          temp2 = curr.next
          temp2.next = head
          head = temp2
          curr.next = None
          
          k -= 1
        
        return head