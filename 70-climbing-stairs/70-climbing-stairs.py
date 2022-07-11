class Solution:
    def climbStairs(self, n: int) -> int:
      # this question is just another form of fibonacci seq
      
      prev2 = 1
      prev = 1
      for i in range(2, n+1):
        curr = prev + prev2
        prev2 = prev
        prev = curr
      
      return prev