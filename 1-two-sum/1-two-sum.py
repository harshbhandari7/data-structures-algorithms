class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        leng = len(nums)
        hash_map = {}
        for i in range(leng):
            diff = target - nums[i]
            if diff in hash_map:
                return [hash_map[diff], i]
            
            hash_map[nums[i]] = i