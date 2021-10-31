nums = list(map(int, input().split()))
target = int(input())

leng = len(nums)
res = [-1, -1]

def find_start_index(nums, target):
	index = -1
	beg = 0
	last = leng
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

def find_end_index(nums, target):
	index = -1
	beg = 0
	last = leng
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

res[0] = find_start_index(nums, target)
res[1] = find_end_index(nums, target)
print(res)
