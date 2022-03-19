class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        leng = len(digits)
        number = 0
        for i, digit in enumerate(digits):
            number += digit * (10 ** ((leng-1) - i))

        number += 1
        res = list(str(number))
        res = list(map(lambda x: int(x), res))
        return res