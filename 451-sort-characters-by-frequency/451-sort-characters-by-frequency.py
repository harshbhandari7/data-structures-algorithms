class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        freq_chars = []
        for key, value in freq.items():
            freq_chars.append(key*value)
        
        freq_chars = sorted(freq_chars, key=len, reverse=True)
        output = ''
        
        for chars in freq_chars:
            output += chars
            
        return output