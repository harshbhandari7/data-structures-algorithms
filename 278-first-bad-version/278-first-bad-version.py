# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 1, n
        while (start < end):
            mid = (start + end) // 2 
            if (not isBadVersion(mid)):
                start = mid + 1
            else:
                end = mid
        
        if (start != n+1 and isBadVersion(start)):
            return start
        return -1