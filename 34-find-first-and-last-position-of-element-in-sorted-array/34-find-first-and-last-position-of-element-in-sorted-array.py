class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        
        res[0] = self.find_start_index(nums, target)
        res[1] = self.find_end_index(nums, target)
        
        return res

    def find_start_index(self, nums, target):
        leng = len(nums)
        index = -1
        beg = 0
        last = leng-1
        while(beg <= last):
            mid = (beg + last) // 2
            if (nums[mid] == target):
                index = mid
                last = mid -1 	# searching the element in the left half now.
            elif(target > nums[mid]):
                beg = mid + 1
            else:
                last = mid -1
        return index

    def find_end_index(self, nums, target):
        leng = len(nums)
        index = -1
        beg = 0
        last = leng-1
        while(beg <= last):
            mid = (beg + last) // 2
            if (nums[mid] == target):
                index = mid
                beg = mid + 1   # searching the element in the right half now.
            elif(target > nums[mid]):
                beg = mid + 1
            else:
                last = mid -1
        return index