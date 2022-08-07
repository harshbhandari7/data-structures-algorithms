class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        leng = len(nums)
        nums.sort()
        
        summ = 0
        for i in range(0, leng, 2):
          summ += nums[i]
        
        return summ
        