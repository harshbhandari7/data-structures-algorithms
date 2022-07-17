class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        leng = len(nums)
        
        if leng == 1:
            return [0, 1]
        
        pairs = 0
        left = 0
        d = {}
        
        for i in range(leng):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        
        for key, value in d.items():
            pairs += value // 2
            left += value % 2 
        
        
        return [pairs, left]