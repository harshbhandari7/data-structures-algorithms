class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        leng = len(nums)
        valid_splits = 0
        left_sum = 0
        right_sum = 0
        
        left_sum = sum(nums)
        
        for i in range(leng-1, 0, -1):
            right_sum += nums[i]
            left_sum -= nums[i]
            
            if (left_sum >= right_sum):
                valid_splits += 1
                
        return valid_splits