class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_set = set()
        for num in nums:
            if num in unique_set:
                return True
            
            unique_set.add(num)
            
        return False