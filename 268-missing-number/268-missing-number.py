class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        leng = len(nums)
        n_sum = leng * (leng+1) // 2
        for num in nums:
            n_sum -= num
        
        return n_sum