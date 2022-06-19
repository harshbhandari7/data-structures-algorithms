class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        leng = len(nums)
        i = 0
        for j in range(leng):
            if (nums[j] != 0):
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        
        
        