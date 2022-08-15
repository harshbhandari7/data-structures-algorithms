class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        sn = s.split()
        leng = len(sn)
        for i in range(leng):
            res.append(sn[i][::-1])
            
        return ' '.join(res)