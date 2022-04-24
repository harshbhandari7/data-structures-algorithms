# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        leng = 0
        curr = head
        while curr:
            leng += 1
            curr = curr.next
        
        mid = leng // 2
        i = 0
        curr2 = head
        while i < mid:
            curr2 = curr2.next
            i += 1
        
        return curr2