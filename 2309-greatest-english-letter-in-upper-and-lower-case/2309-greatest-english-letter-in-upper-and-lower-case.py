class Solution:
    def greatestLetter(self, s: str) -> str:
        leng = len(s)
        if leng == 1:
            return ''
        greatest_char = []
        char_hash = {}
        
        for i in range(1, leng):
            if (ord(s[i]) < 91 and ord(s[i])+32 in char_hash):
                greatest_char.append(ord(s[i]))
            elif(ord(s[i]) > 96 and ord(s[i]) - 32 in char_hash):
                greatest_char.append(ord(s[i])-32)
            char_hash[ord(s[i])] = 1
            
        greatest_char.sort()
        return chr(greatest_char[-1]) if len(greatest_char) else ""