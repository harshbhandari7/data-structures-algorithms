class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        leng = len(nums)
        slow = 0
        for fast in range(leng):
          if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
        
        return slow