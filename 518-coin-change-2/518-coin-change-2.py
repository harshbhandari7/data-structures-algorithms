class Solution:
    def get_count(self, ind, coins, target, memo):
      if ind == 0:
        if target % coins[ind] == 0:
          return 1
        
        return 0
      
      if (ind, target) in memo:
        return memo[(ind, target)]
      
      not_take = self.get_count(ind-1, coins, target, memo)
      take = 0
      if coins[ind] <= target:
        take = self.get_count(ind, coins, target-coins[ind], memo)
      
      summ = take + not_take
      memo[(ind, target)] = summ
      return summ
        
    def change(self, amount: int, coins: List[int]) -> int:
      leng = len(coins)
      memo = {}
      return self.get_count(leng-1, coins, amount, memo)