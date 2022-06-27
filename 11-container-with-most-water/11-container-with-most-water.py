class Solution:
    def maxArea(self, height: List[int]) -> int:
        leng = len(height)
        start, end = 0, leng - 1
        max_water = 0
        for i in range(leng-1, 0,-1):
            if height[start] > height[end]:
                max_water = max(max_water, i * height[end])
                end -= 1
            else:
                max_water = max(max_water, i * height[start])
                start += 1
        return max_water