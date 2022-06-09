class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        leng = len(nums)
        res = nums[0]
        for i in range(1, leng):
            res = res ^ nums[i]
        
        return res