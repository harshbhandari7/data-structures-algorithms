class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False

        char_map = {}
        for s_char, t_char in zip(s, t):
            char_map[s_char] = t_char
        
        new_s = ''
        for char in s:
            new_s += char_map[char]

        return new_s == t