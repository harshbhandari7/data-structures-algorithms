class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        leng = len(nums)
        if leng == 1:
            return nums[0]
        
        max_sum = float('-inf')
        current_sum = 0
        
        for ele in nums:
            current_sum += ele
            if (current_sum > max_sum):
                max_sum = current_sum
            if (current_sum < 0):
                current_sum = 0
                
        return max_sum 