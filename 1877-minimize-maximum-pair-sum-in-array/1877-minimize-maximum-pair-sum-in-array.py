class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        leng = len(nums)
        nums.sort()
        max_sum = nums[-2] + nums[-1]
        pairs = []
        start, end = 0, leng-1
        while(start < end):
            if (nums[start] + nums[end]):
                pairs.append((nums[start], nums[end]))
                start += 1
                end -=1
        pairs_sum = list(map(lambda x: x[0] + x[1], pairs))
        
        return max(pairs_sum)