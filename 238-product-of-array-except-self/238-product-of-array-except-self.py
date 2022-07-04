class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leng = len(nums)
        product = [1] * leng
        left = [1] * leng
        right = [1] * leng
        
        for i in range(1, leng):
            left[i] = left[i-1] * nums[i-1]
            
        for i in range(leng-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        
        for i in range(leng):
            product[i] = left[i] * right[i]
            
        return product