# ----------- Functional recusrion problems ------------

# reverse an array

arr = [1, 2, 3, 4 ,5, 6]
leng = len(arr)

def reverse_num(i):
	if i >= (leng//2):
		return

	arr[i], arr[leng-i-1] = arr[leng-i-1], arr[i]
	return reverse_num(i+1)

reverse_num(0)
print(arr)

# string is palindrome or not
s = 'nayan'
leng  =len(s)
def is_palindrome(i):
	if i >= (leng // 2):
		return True

	if s[i] != s[leng-i-1]:
		return False

	return is_palindrome(i+1)

print(is_palindrome(0))