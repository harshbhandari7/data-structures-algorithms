class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leng = len(nums)
        left_sum, right_sum = 0, sum(nums)
        for i in range(leng):
            right_sum -= nums[i]
            
            if (left_sum == right_sum):
                return i
            left_sum += nums[i]
        
        return -1