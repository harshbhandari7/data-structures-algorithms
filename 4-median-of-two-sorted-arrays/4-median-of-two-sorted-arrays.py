class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        arr = [None] * (m + n)
        i = j = k = 0
        while i < m and j < n:
          if nums1[i] < nums2[j]:
            arr[k] = nums1[i]
            i += 1
          else:
            arr[k] = nums2[j]
            j += 1
          
          k += 1
        
        while i < m:
          arr[k] = nums1[i]
          i += 1
          k += 1
        
        while j < n:
          arr[k] = nums2[j]
          j += 1
          k += 1
        
        if (m+n) % 2 == 0:
          mid = (m+n) // 2
          median = (arr[mid-1] + arr[mid]) / 2
          return median
        else:
          return arr[(m+n) // 2]