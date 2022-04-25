# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        node_hash = {}
        while curr:
            if curr.val not in node_hash:
                node_hash[curr.val] = ListNode(curr.val)
            
            curr = curr.next

        dummy = curr2 = ListNode(0)
        for key in node_hash:
            curr2.next = node_hash[key]
            curr2 = curr2.next
        
        
        return dummy.next
        