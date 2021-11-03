'''
You are given an n x n 2D matrix representing an image,
rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify
the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.
'''

n=int(input())
matrix = [[int(input()) for y in range(n)] for x in range(n)]

for i in range(n):
	for j in range(i, n):
		matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]  # transpose

# reversing the elements of transpose will give us the 90 deg image.
for i in range(n):
	matrix[i] = matrix[i][::-1]

print(matrix)