class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key_map = { ' ': ' ' }
        ch = 97
        decoded = ''
        for s in key:
            if s not in key_map:
                key_map[s] = chr(ch)
                ch += 1
        
        for s in message:
            if s in key_map:
                decoded += key_map[s]
        
        return decoded