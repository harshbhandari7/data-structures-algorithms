class Solution:
    def fib(self, n: int) -> int:
        x, y = 0, 1
        while n > 0:
            x, y = y, x+y
            n -= 1
        return x