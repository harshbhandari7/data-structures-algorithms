def merge_array(nums1, nums2, m, n):
	if (n == 0):
		return nums1
	while m > 0 and n > 0:
		if nums1[m - 1] > nums2[n - 1]:
			nums1[m + n - 1] = nums1[m - 1]
			m -= 1
		else:
			nums1[m + n - 1] = nums2[n - 1]
			n -= 1
	nums1[:n] = nums2[:n]
	return nums1


nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

m = int(input())
n = int(input())

print(merge_array(nums1, nums2, m, n))
