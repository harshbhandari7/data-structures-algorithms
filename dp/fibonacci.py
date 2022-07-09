# 1. memoization

def fibo_memo(n, dp):
	if n <= 1:
		return n

	if dp[n] != -1:
		return dp[n]

	return fibo_memo(n-1, dp) + fibo_memo(n-2, dp)

n = 7
dp = [-1] * (n+1)
print('Fiboncci using memoization - ', fibo_memo(n, dp))

# Time complexity - O(n)
# Space complexity - O(n) [ O(n) recursion stack + O(n) for dp array = O(2n)]

# 2. Tabulation

n1 = 7
dp1 = [-1] * (n1 + 1)

dp1[0], dp1[1] = 0, 1
for i in range(2, n1+1):
	dp1[i] = dp1[i-1] + dp1[i-2]

print('Fiboncci using tabulation - ', dp1[n1])

# Time complexity - O(n)
# Space complexity - O(n) [ Just O(n) for dp array]

# 3. Space optimisation

n3 = 0
prev2 = 0
prev = 1

for i in range(2, n3+1):
	curr = prev2 + prev
	prev2 = prev
	prev = curr

print('Fibonacci after space optimisation - ', prev if n3 != 0 else 0 )

# Time complexity - O(n)
# Space complexity - O(1)