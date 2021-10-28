arr = list(map(int, input().split()))
leng = len(arr)

max_e, min_e = arr[0], arr[0]

for ele in arr:
	if ele > max_e:
		max_e = ele
	elif ele < min_e:
		min_e = ele

print(max_e, min_e)