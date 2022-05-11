matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 20

def search_matrix(matrix, target):
	leng = len(matrix)

	if leng < 2:
		if target in matrix[0]:
			return True

		return False

	midR = leng // 2
	midC = len(matrix[0]) // 2

	mid_ele = matrix[midR][midC]

	if target <= mid_ele:
		


print(search_matrix(matrix, target))