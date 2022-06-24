class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        leng = len(nums)
        if leng < 3:
            return []
        
        nums.sort()
        triplet_set = set()
        
        for i in range(leng):
            start = i + 1
            end = leng - 1
            target = 0 - nums[i]
            
            while start < end:
                if target == nums[start] + nums[end]:
                    triplet_set.add((nums[i], nums[start], nums[end]))
                    start += 1
                    end -= 1
                elif(nums[start] + nums[end] < target):
                    start += 1
                else:
                    end -= 1
        
        triplet_list = [list(s) for s in triplet_set]
        return triplet_list
                
            
            