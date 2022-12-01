class Solution:
    def halvesAreAlike(self, s: str) -> bool:
      leng = len(s)
      start, end = 0, leng-1
      ctr = 0
      vowels = set('aeiouAEIOU')

      while start < end:
        if s[start] in vowels:
          ctr += 1
        if s[end] in vowels:
          ctr -= 1

        start += 1
        end -= 1

      return ctr == 0