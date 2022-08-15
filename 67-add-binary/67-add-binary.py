class Solution:
    def get_binary(self, bin):
      leng = len(bin)
      deci = 0
      power = leng - 1
      for i in range(leng):
        deci += int(bin[i]) * (2 ** power)
        power -= 1
        
      return deci
    
    def get_decimal(self, deci):
      bin = ""
      while deci > 1:
        bin += str(deci % 2)
        deci = deci // 2
      
      bin += str(deci)
      
      return bin[::-1]
        
    def addBinary(self, a: str, b: str) -> str:
        a_deci = self.get_binary(a)
        b_deci = self.get_binary(b)
        
        summ = a_deci + b_deci
        summ_bin = self.get_decimal(summ)
        
        return summ_bin