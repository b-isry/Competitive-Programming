# Last updated: 8/3/2026, 9:20:21 PM
1class Solution:
2    def stoneGameIII(self, stoneValue: List[int]) -> str:
3        n = len(stoneValue)
4
5        dp = [0] * (n + 1)
6
7        for i in range(n - 1, -1, -1):
8            best = float("-inf")
9            take = 0
10
11            for k in range(3):
12                if i + k < n:
13                    take += stoneValue[i + k]
14                    best = max(best, take - dp[i + k + 1])
15
16            dp[i] = best
17
18        if dp[0] > 0:
19            return "Alice"
20        elif dp[0] < 0:
21            return "Bob"
22        return "Tie"