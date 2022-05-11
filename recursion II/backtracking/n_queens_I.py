class NQueens:
	def is_safe(self, row, col, board, n):
		ROW = row
		COL = col
		while (row >= 0 and col >= 0):
			if board[row][col] == 'Q':
				return False
			row -= 1
			col -= 1

		row = ROW
		col = COL
		while (col >= 0):
			if board[row][col] == 'Q':
				return False
			col -= 1

		row = ROW
		col = COL

		while (row < n and col >= 0):
			if board[row][col] == 'Q':
				return False
			row += 1
			col -= 1

		return True

	def get_board_pos(self, col, board, ans, n):
		if col == n:
			temp = []
			for i in range(n):
				ans_str = ''
				for j in range(n):
					ans_str += board[i][j]
				temp.append(ans_str)
			ans.append(temp)
			return

		for row in range(n):
			if self.is_safe(row, col, board, n):
				board[row][col] = 'Q'
				self.get_board_pos(col+1, board, ans, n)
				board[row][col] = '.'

	def solve_n_queens(self, n):
		if n == 1:
			return [["Q"]]

		ans = []
		board = [["." for i in range(n)] for i in range(n)]
		self.get_board_pos(0, board, ans, n)

		return ans

obj = NQueens()
print(obj.solve_n_queens(4))
