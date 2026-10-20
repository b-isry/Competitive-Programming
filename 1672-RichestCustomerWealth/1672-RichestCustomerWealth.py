# Last updated: 10/20/2026, 8:57:59 PM
1class Solution:
2    def maximumWealth(self, accounts: list[list[int]]) -> int:
3        max_wealth = 0
4
5        for customer in accounts:
6            wealth = sum(customer)
7            max_wealth = max(max_wealth, wealth)
8
9        return max_wealth