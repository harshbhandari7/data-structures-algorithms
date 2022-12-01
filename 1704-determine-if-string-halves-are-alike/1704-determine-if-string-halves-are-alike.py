class Solution:
    def halvesAreAlike(self, s: str) -> bool:
      leng = len(s)
      start, end = 0, leng-1
      f = sec = 0
      vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

      while start < end:
        if s[start] in vowels:
          f += 1
        if s[end] in vowels:
          sec += 1

        start += 1
        end -= 1

      return f == sec