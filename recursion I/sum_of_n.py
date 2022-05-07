# approach 1 - parameterised

def get_n_sum(i, summ):
	if i < 1:
		print(summ)
		return

	summ += i
	get_n_sum(i-1, summ)

get_n_sum(3, 0)

# approach 2 - functional

def get_sum_n(n):
	if n == 0:
		return 0

	return n + get_sum_n(n-1)

print('functional -', get_sum_n(3))