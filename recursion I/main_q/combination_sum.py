# Combination sum I

arr = [2, 3, 6, 7]
target = 7
leng = len(arr)
res = []
	
def get_combo_sum(ind, seq, target):
	if ind == leng:
		if target == 0:
			temp = seq.copy()
			res.append(temp)
		return

	# case where we have picked the element
	if arr[ind] <= target:
		seq.append(arr[ind])
		get_combo_sum(ind, seq, target-arr[ind])
		seq.remove(arr[ind])

	# case where we have not picked the element
	get_combo_sum(ind+1, seq, target)

get_combo_sum(0, [], target)
print(res)