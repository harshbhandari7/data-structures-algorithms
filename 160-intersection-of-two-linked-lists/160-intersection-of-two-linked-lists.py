# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA == None or headB == None:
            return None
        
        currA = headA
        currB = headB
        
        while (currA != currB):
            
            currA = headB if currA == None else currA.next
            currB = headA if currB == None else currB.next
        
        return currA
        
# This approach takes O(m) space.
#         currA = headA
#         currB = headB
#         hash_A = {}
        
#         while(currA):
#             hash_A[currA] = currA
#             currA = currA.next
            
#         while(currB):
#             if (currB in hash_A):
#                 return currB
            
#             currB = currB.next
            
#         return None