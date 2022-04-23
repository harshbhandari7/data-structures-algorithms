# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head and head.next == None and n == 1:
            return None
        
        leng = 0
        curr = head
        while(curr):
            curr = curr.next
            leng += 1
        
        del_pos = leng - n
        
        curr2 = head
        if (del_pos == 0):
            head = curr2.next
            return head
        
        i = 1
        while (i < del_pos):
            curr2 = curr2.next
            i += 1
        
        temp = curr2.next
        curr2.next = curr2.next.next
        temp.next = None
        
        return head