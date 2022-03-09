class Solution:
    def reverse(self, x: int) -> int:
        num = abs(x)
        reverse_list = []
        while (num != 0):
            reverse_list.append(num % 10)
            num = num // 10

        leng = len(reverse_list)
        reverse_num = 0

        for i in range(leng):
            reverse_num += reverse_list[i] * pow(10, (leng-1)-i)

        if (x < 0):
            reverse_num = -1 * reverse_num
            
        if (not(abs(reverse_num) < 2**31 and reverse_num >= -2**31)):
            reverse_num = 0
            
        return reverse_num