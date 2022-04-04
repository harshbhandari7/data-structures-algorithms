class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        leng = len(nums)
        start, end = 0, leng - 1
        while (start < end):
            mid = (start + end) // 2
            if (nums[mid] > nums[mid+1] and nums[mid-1] < nums[mid]):
                return mid
            elif (nums[mid] < nums[mid+1]):
                start = mid + 1
            else:
                end = mid - 1

        return start