class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(1, numRows+1):
            res.append([ -1 ] * i)
        res[0][0] = 1
        for i in range(1, len(res)):
            res[i][0], res[i][-1] = 1, 1
            for j in range(1, len(res[i])-1):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res