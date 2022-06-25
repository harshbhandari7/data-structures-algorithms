class Solution:
    def countAsterisks(self, s: str) -> int:
        leng = len(s)
        isStart = False
        ctr = 0
        for i in range(leng):
            if (not isStart and s[i] == '*'):
                ctr += 1
            elif (s[i] == '|'):
                isStart = not isStart
        
        return ctr