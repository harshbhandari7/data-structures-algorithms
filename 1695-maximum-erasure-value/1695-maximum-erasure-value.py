class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        leng = len(nums)
        n_hash = set()
        l = 0
        l = curr_sum = max_sum = 0
        
        for i in range(leng):
            while nums[i] in n_hash:
                curr_sum -= nums[l]
                n_hash.remove(nums[l])
                l += 1
            
            curr_sum += nums[i]
            n_hash.add(nums[i])
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
                                   
                
        