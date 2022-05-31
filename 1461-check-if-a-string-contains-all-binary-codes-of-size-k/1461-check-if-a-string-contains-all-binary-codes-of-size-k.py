class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        leng  = len(s)
        combos = set()
        for i in range(leng-k+1):
            combos.add(s[i:i+k])
        
        return len(combos) == 2**k