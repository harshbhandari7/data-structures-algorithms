class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        leng = len(nums)
        k = 0
        for i in range(0, leng):
            if (nums[i] != val):
                nums[k] = nums[i]
                k += 1
        return k