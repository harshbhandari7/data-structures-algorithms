class Solution:
    def __init__(self):
        self.res = []
        
    def get_combo_sum(self, ind, seq, target, arr):
        if ind == len(arr):
            if target == 0:
                temp = seq.copy()
                self.res.append(temp)
            return

        # case where we have picked the element
        if arr[ind] <= target:
            seq.append(arr[ind])
            self.get_combo_sum(ind, seq, target-arr[ind], arr)
            seq.remove(arr[ind])

        # case where we have not picked the element
        self.get_combo_sum(ind+1, seq, target, arr)
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.get_combo_sum(0, [], target, candidates)
        return self.res