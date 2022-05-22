class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        if letter not in s:
            return 0
        
        leng = len(s)
        ctr = 0
        for char in s:
            if char == letter:
                ctr += 1
                
        return math.floor((ctr / leng) * 100)