class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leng = len(prices)
        left = 0
        right = 1
        max_profit = 0
        while right < leng:
          curr = prices[right] - prices[left]
          if prices[left] < prices[right]:
            max_profit = max(curr, max_profit)
          
          else:
            left = right
          
          right += 1
        
        return max_profit
            
          