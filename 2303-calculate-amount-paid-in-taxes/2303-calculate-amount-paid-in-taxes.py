class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        leng = len(brackets)
        if income == 0:
            return float(0)
        
        tax = 0
        if (income > brackets[0][0]):
            tax = brackets[0][0] * (brackets[0][1] * 0.01)
        else:
            tax = income * (brackets[0][1] * 0.01)
            
        rem_inc = income - brackets[0][0]
        
        i = 1
        while rem_inc > 0 and i < leng:
            principal = (brackets[i][0] - brackets[i-1][0]) if brackets[i][0] <= income else (income - brackets[i-1][0])
            rem_inc -= principal
            tax += principal * (brackets[i][1] * 0.01)
            i += 1
            
        return tax