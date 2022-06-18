class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        leng = len(nums)
        k = k % leng
        if k > 0 and leng > 1:
            nums[:] = nums[-k:] + nums[:-k]
            