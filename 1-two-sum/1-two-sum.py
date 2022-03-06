class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        leng=len(nums)
        res1 = {}
        for i in range(leng):
            foo = target - nums[i]
            if foo in res1:
                return [res1[foo], i]
            res1[nums[i]] = i