class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        leng = len(nums)
        if leng == 1:
            return nums[0]
        
        nums_hash = {}
        for ele in nums:
            if ele in nums_hash:
                nums_hash[ele] += 1
            else:
                nums_hash[ele] = 1
                
                
        for ele in nums:
            if nums_hash[ele] == 1:
                return ele