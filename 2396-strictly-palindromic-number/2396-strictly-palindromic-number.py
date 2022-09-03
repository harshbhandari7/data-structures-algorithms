class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        last_base = n - 2
        curr_base = 2
        
        while curr_base <= last_base:
          temp = n
          s = ''
          while temp >= curr_base:
            r = temp % curr_base
            s += str(r)
            temp = temp // curr_base
            
          s += str(temp)
          s = s[::-1]

          if s != s[::-1]:
            return False
          
          curr_base += 1
        
        return True