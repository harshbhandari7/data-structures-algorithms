class Solution:
    def romanToInt(self, s: str) -> int:
        str_len = len(s)
        roman_chars = {'I':1, 'V':5, 'X': 10, 'L':50, 'C':100, 'D':500,'M':1000}
        res = 0
        for i in range(str_len - 1):
            if roman_chars[s[i]] < roman_chars[s[i+1]]:
                res -= roman_chars[s[i]]
            else:
                res += roman_chars[s[i]]
        res += roman_chars[s[-1]]
        return res