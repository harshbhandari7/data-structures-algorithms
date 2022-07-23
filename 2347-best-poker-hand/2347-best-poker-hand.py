class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        memo = {}
        for rank in ranks:
            if rank in memo:
                memo[rank] += 1
            else:
                memo[rank] = 1
        
        if len(set(suits)) == 1:
            return 'Flush'
        
        hand = 'High Card'
        val = 0
        for key, value in memo.items():
            if value > val and value >= 3:
                hand = 'Three of a Kind'
                val = value
                break
            elif value > val and value == 2:
                hand = 'Pair'
                val = value
        
        return hand