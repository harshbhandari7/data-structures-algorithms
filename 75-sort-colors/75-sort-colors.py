class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        leng = len(nums)
        c0 = 0
        c2 = leng - 1
        ind = ctr = 0
        
        while ctr < leng:
          if nums[ind] == 0:
            nums[ind], nums[c0] = nums[c0], nums[ind]
            ind += 1
            c0 += 1
            
          elif nums[ind] == 1:
            ind += 1
          
          else:
            nums[ind], nums[c2] = nums[c2], nums[ind]
            c2 -= 1
            
          ctr += 1
        