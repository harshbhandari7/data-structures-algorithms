# Number of Subsequences That Satisfy the Given Sum Condition

arr = [2, 3, 3, 4, 6, 7]
leng = len(arr)
target = 12
op = []

def get_subsequence(ind, seq):
	if ind >= leng:
		if len(seq) and ((min(seq) + max(seq)) <= target):
			op.append(seq)
		return

	seq.append(arr[ind])
	get_subsequence(ind+1, seq)

	seq.remove(arr[ind])
	get_subsequence(ind+1, seq)

get_subsequence(0, [])
print(len(op))