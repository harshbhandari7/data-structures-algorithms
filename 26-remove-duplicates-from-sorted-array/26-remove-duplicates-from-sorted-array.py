class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ind = 1
        leng = len(nums)
        prev = nums[0]
        for i in range(1, leng):
          if nums[i] == prev:
            continue
          else:
            nums[ind] = nums[i]
            ind += 1
            prev = nums[i]
        
        return ind