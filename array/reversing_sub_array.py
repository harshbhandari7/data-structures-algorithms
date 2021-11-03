'''
Given two integer arrays of equal length target and arr.
In one step, you can select any non-empty sub-array of arr and reverse it.
You are allowed to make any number of steps.
Return True if you can make arr equal to target, or False otherwise.
'''

def is_array_equal(arr, target):
	leng = len(arr)
	target_dict = {}
	arr_dict = {}
	    
	for ele in arr:
	    if ele in arr_dict:
	        arr_dict[ele] += 1
	    else:
	        arr_dict[ele] = 1

	for ele in target:
	    if ele in target_dict:
	        target_dict[ele] += 1
	    else:
	        target_dict[ele] = 1
	        
	return arr_dict == target_dict

arr = list(map(int, input().split()))
target = list(map(int, input().split()))

print(is_array_equal(arr, target))