class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return words
        
        i = 1
        while i < len(words):
            second = sorted(words[i])
            first = sorted(words[i-1])
            
            if second == first:
                words.pop(i)
            else:
                i += 1
            
        return words