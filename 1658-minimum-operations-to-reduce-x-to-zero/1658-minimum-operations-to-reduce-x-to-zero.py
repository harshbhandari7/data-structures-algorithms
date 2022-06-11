class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums)-x
        leng = len(nums)

        if target < 0: return -1
        if target == 0: return leng
        
        start = 0
        curr_sum = 0
        n_target = -1
        
        for i in range(leng):
            if curr_sum < target:
                curr_sum += nums[i]
            while curr_sum >= target:
                if curr_sum == target:
                    n_target = max(n_target, i-start+1)
                curr_sum -= nums[start]
                start += 1
        
        return leng-n_target if n_target != -1 else -1