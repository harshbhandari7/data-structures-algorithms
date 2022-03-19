class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        leng = len(nums)
        max_num, max_num_ind = nums[0], 0
        for i in range(1, leng):
            if (nums[i] > max_num):
                max_num = nums[i]
                max_num_ind = i
        for i in range(leng):
            if (i != max_num_ind and max_num < 2*nums[i]):
                return -1
        return max_num_ind