class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        leng = len(nums)
        nums_sum = []
        
        for i in range(leng):
            summ = sum(nums[:i+1])
            nums_sum.append(summ)
            
        return nums_sum