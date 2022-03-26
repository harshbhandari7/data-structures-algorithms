class Solution:
    def search(self, nums: List[int], target: int) -> int:
        leng = len(nums)
        start, end = 0, leng-1
        while (start <= end):
            mid = start + (end-start) // 2
            if (target == nums[mid]):
                return mid
            elif(target > nums[mid]):
                start = mid + 1
            else:
                end = mid - 1
        
        return -1