class Solution:
    def reverse(self, nums, start, end):
      while start < end:
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        
        start += 1
        end -= 1
      
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # approach 1 TC (n * k), SC O(1)
        # leng = len(nums)
        # for i in range(k):
        #   prev = nums[-1]
        #   for j in range(leng):
        #     curr = nums[j]
        #     nums[j] = prev
        #     prev = curr
        
        # approach 2 TC O(n) SC O(1)
        leng = len(nums)
        k %= leng # if k > leng we will need to rotate only remainder times else k times
        # first reverse the whole array
        self.reverse(nums, 0, leng - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, leng - 1)
        