class Solution:
    def __init__(self):
      self.res = []
    
    def get_combi(self, i, nums, target, seq):
      if i == len(nums):
        if target == 0:
          temp = seq.copy()
          self.res.append(temp)
        return
      
      if target > 0:
        seq.append(nums[i])
        self.get_combi(i, nums, target-nums[i], seq)
        seq.remove(nums[i])
        
      self.get_combi(i+1, nums, target, seq)
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
      self.get_combi(0, candidates, target, [])
      return self.res