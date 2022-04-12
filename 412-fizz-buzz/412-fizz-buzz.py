class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        for i in range(1, n+1):
            s = ''
            if (i % 3 == 0):
                s += 'Fizz'
            if (i % 5 == 0):
                s += 'Buzz'
            output.append(f"{i}" if s == '' else s)
        return output