# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_sub_tree(self, nums, start, end):
        if start == end:
            return None
        
        mid = (start + end) // 2
        
        node = TreeNode(nums[mid])
        node.left = self.get_sub_tree(nums, start, mid)
        node.right = self.get_sub_tree(nums, mid+1, end)
        
        return node
        
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.get_sub_tree(nums, 0, len(nums))