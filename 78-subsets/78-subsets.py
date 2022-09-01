class Solution:
    def get_permutation(self, i, nums, seq, res):
        if i >= len(nums):
          res.append(seq.copy())
          return

        seq.append(nums[i])
        self.get_permutation(i+1, nums, seq, res)

        seq.remove(nums[i])
        self.get_permutation(i+1, nums, seq, res)
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.get_permutation(0, nums, [], res)
        
        return res