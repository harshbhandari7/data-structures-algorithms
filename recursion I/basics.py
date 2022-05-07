# ---------------- Example 1 --------------
# s = input()

# def print_name_n_times(name, n):
# 	if n > 5:
# 		return None

# 	print('Name is ', name)

# 	print_name_n_times(name, n+1)

# print_name_n_times(s, 1)

# ---------------- Example 2 ---------------
# 1 to n 

# def print_digits(i, n):
# 	if i > n:
# 		return

# 	print(i, end=' ')
# 	print_digits(i+1, n)

# print_digits(1, 5)

# ---------------- Example 3 ---------------
# print 1 to N by back tracking

def print_backtrack(i, n):
	if i < 1:
		return

	print_backtrack(i-1, n)
	print(i, end=" ")

print_backtrack(5, 5) 

# print N to 1

# def print_backtrack_n(i, n):
# 	if i > n:
# 		return

# 	print_backtrack_n(i+1, n)
# 	print(i, end=" ")

# print_backtrack_n(1, 5)


