# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        if not head.next or not head.next.next:
            return head
        
        odd_n = odd_head = head
        even_n = even_head = head.next
        
        while (even_n and even_n.next):
            odd_n.next = odd_n.next.next
            even_n.next = even_n.next.next
            
            odd_n = odd_n.next
            even_n = even_n.next
            
            
        odd_n.next = even_head
        
        return odd_head