# This code generates all the subsequences of a sequence

# Also, it is a general template for subsequence problems using recursion

arr = [3, 1, 2, 4]
leng = len(arr)

def get_subsequence(ind, seq):
	if ind >= leng:
		print(seq)
		return

	seq.append(arr[ind])
	get_subsequence(ind+1, seq)

	seq.remove(arr[ind])
	get_subsequence(ind+1, seq)

get_subsequence(0, [])