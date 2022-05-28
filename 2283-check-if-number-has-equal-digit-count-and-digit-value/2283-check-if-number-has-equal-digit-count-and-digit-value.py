class Solution:
    def digitCount(self, num: str) -> bool:
        leng = len(num)
        freq = {}
        
        for i in range(leng):
            freq[str(i)] = 0
            
        for i in range(leng):
            if num[i] in freq:
                freq[num[i]] += 1
        
        print(freq)
        for i in range(leng):
            if num[i] == str(freq[str(i)]):
                continue
            else:
                return False
            
        return True