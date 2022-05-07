# fibonacci no using recusrion

def fibonacci(n):
	if n < 2:
		return n

	return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7))

# fibonacci using memoization

memo = { 1: 0, 2: 1 }
def fib_memo(n):
	if n < 2:
		memo[n] = n
		return n

	if n in memo:
		return memo[n]

	fib_sum = fib_memo(n-2) + fib_memo(n-1)
	memo[n] = fib_sum
	return fib_sum

print(fib_memo(7))

