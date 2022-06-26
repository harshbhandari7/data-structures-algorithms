class Solution:
    def countHousePlacements(self, n: int) -> int:
        sequence = [-1] * (n+2)
        
        sequence[0] = 1
        sequence[1] = 2
        
        for i in range(2, n+1):
            sequence[i] = sequence[i - 1] + sequence[i - 2]
        
        return (sequence[n] * sequence[n]) % (10 ** 9 + 7) 
        
                