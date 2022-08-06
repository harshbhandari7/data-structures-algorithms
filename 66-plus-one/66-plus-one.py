class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        for d in digits:
          s += str(d)
        n = int(s)
        n += 1
        s = str(n)
        res = []
        for ch in s:
          res.append(int(ch))
        
        return res