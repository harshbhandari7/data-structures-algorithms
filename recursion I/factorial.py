# factorial of n

def get_n_factorial(n):
	if n < 2:
		return 1

	return n * get_n_factorial(n-1)

print(get_n_factorial(-5))