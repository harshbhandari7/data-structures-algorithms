class Solution:
    def __init__(self):
        self.res = []
        
    def get_subsequence(self, ind, seq, nums):
        if ind >= len(nums):
            temp = seq.copy()
            self.res.append(temp)
            return
        
        seq.append(nums[ind])
        self.get_subsequence(ind+1, seq, nums)
        
        seq.remove(nums[ind])
        self.get_subsequence(ind+1, seq, nums)
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.get_subsequence(0, [], nums)
        return self.res
        
        
        