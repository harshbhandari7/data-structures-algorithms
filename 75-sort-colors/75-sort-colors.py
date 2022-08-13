class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        leng = len(nums)
        zero = one = 0
        for n in nums:
          if n == 0:
            zero += 1
          if n == 1:
            one += 1
        
        two = leng - one - zero
        
        nums[: zero] = [0] * zero
        nums[zero: zero + one] = [1] * one
        nums[zero + one:] = [2] * two
        