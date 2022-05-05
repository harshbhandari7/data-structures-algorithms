class Solution:
    def __init__(self):
        self.permutations = []

    def get_permutations(self, seq, arr, freq):
        if len(arr) == len(seq):
            temp = seq.copy()
            self.permutations.append(temp)
            return
        for i in range(len(arr)):
            if not(i in freq and freq[i]):
                freq[i] = True
                seq.append(arr[i])
                self.get_permutations(seq, arr, freq)
                seq.remove(seq[len(seq) - 1])
                freq[i] = False

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.get_permutations([], nums, {})
        return self.permutations