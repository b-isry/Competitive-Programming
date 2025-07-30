# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        profit = 0

        for i in prices:
            if i < min_price:
                min_price = i
            else:
                profit = max(profit, i - min_price)
        
        return profit