# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        leng = 0
        temp = head
        while temp:
            leng += 1
            temp = temp.next
        
        if k >= leng:
            k = k % leng
        
        break_point = leng - k
        
        if break_point == leng:
            return head
        
        curr = head
        for i in range(break_point-1):
            curr = curr.next
            
        temp2 = curr.next
        
        while temp2 and temp2.next:
            temp2 = temp2.next
            
        temp2.next = head
        head = curr.next
        curr.next = None
        
        return head