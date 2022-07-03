class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        leng = len(nums)
        nums_sum = [nums[0]]
        
        for i in range(1, leng):
            nums_sum.append(nums_sum[-1] + nums[i])
            
        return nums_sum