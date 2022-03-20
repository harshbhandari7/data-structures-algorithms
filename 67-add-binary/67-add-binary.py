class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_num = 0
        b_num = 0
        a_pos = len(a) - 1
        for bit in a:
            a_num += int(bit) * (2 ** a_pos)
            a_pos -= 1
        
        b_pos = len(b) - 1
        for bit in b:
            b_num += int(bit) * (2 ** b_pos)
            b_pos -= 1
        
        num_sum = a_num + b_num
        
        if (num_sum == 0):
            return '0'
        
        binary_sum = ''
        
        while (num_sum > 0):
            rem = num_sum % 2
            binary_sum += str(rem)
            num_sum = num_sum // 2
        
        return binary_sum[::-1]