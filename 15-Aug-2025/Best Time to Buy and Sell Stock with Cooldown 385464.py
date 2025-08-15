# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       
       cache = {}
       def dp(index, transaction, bought):
          if index == len(prices) or transaction > 1:
            return 0
          state = (index, transaction, bought)
          if state not in memo:
            buy = sell = 0
            if bought == True:
              sell = prices[index] + dp(index +1, transaction + 1, False)
            else:
               buy = -prices[index] + dp(index+1,transaction, True)
            leave = dp(index  +1, transaction, bought)
            cache[state] = max(buy, sell, leave)
          return cache[state]
      return dp(0,0,False)
