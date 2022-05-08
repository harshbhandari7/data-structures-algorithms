class Solution:
    def merge(self, L, R, nums):
        i = j = k = 0
        while(i < len(L) and j < len(R)):
            if L[i] < R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            nums[k] = L[i]
            k += 1
            i += 1
        
        while j < len(R):
            nums[k] = R[j]
            k += 1
            j += 1
    
    def merge_sort(self, nums):
        if len(nums) < 2:
            return nums
        
        mid = len(nums) // 2
        
        L = nums[:mid]
        R = nums[mid:]
        
        self.merge_sort(L)
        self.merge_sort(R)
        self.merge(L, R, nums)
        
        return nums
    
        return nums
    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums)
        return nums