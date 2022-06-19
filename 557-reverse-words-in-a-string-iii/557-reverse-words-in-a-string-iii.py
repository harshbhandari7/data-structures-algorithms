class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        sn = s.split()
        leng = len(sn)
        for i in range(leng):
            snc = [None] * len(sn[i])
            start = 0
            end = len(snc) - 1
            while start <= end:
                snc[start], snc[end] = sn[i][end], sn[i][start]
                start += 1
                end -= 1
                
            res.append(''.join(snc))
        
        return ' '.join(res)