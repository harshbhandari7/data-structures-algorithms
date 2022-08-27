# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = n2 = ''
        while l1:
          n1 += str(l1.val)
          l1 = l1.next
        
        while l2:
          n2 += str(l2.val)
          l2 = l2.next
        
        n1 = int(n1[::-1])
        n2 = int(n2[::-1])
        
        n = str(n1 + n2)[::-1]
        
        dumm = curr = ListNode()
        for i in range(len(n)):
          curr.next = ListNode(int(n[i]))
          curr = curr.next
        
        return dumm.next
        
        
        