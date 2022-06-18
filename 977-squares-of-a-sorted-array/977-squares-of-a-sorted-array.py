class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        leng = len(nums)
        res = [None] * leng
        left, right = 0, leng-1
        
        for i in range(leng-1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                res[i] = nums[left] ** 2
                left += 1
            else:
                res[i] = nums[right] ** 2
                right -= 1
        
        
        return res