class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1: return 1
        start = 0
        end = x
        while (start <= end):
            mid = start + (end - start) // 2
            if (mid * mid <= x < (mid+1) * (mid+1)):
                return mid
            elif (x < mid * mid):
                end = mid -1
            else:
                start = mid +1