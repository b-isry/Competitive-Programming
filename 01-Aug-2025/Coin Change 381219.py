# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(amt):
            if amt in memo:
                return memo[amt]
            if amt == 0:
                return 0
            if amt < 0:
                return float('inf')

            min_cnt = float('inf')
            for i in coins:
                res = dp(amt - i)
                if res != float('inf'):
                    min_cnt = min(min_cnt, res + 1)

            memo[amt] = min_cnt
            return memo[amt]
        cnt = dp(amount)         
        return cnt if cnt != float('inf') else -1

            