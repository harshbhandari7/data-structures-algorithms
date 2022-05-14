class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_s = str(num)
        output = 0
        for i in range(len(num_s) - k + 1):
            divisor = int(num_s[i:i+k])
            if (divisor != 0) and (num % divisor == 0):
                output += 1
        
        return output