class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        
        ctr = 0
        while num:
            if num % 2 == 0:
                num = num // 2
            else:
                num -= 1
            ctr += 1
        
        return ctr