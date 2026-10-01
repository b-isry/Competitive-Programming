# Last updated: 10/1/2026, 11:02:50 PM
1class Solution:
2    def countTexts(self, pressedKeys: str) -> int:
3        MOD = 10**9 + 7
4        n = len(pressedKeys)
5
6        dp = [0] * (n + 1)
7        dp[0] = 1
8
9        for i in range(1, n + 1):
10            dp[i] = dp[i - 1]
11
12            if i >= 2 and pressedKeys[i - 1] == pressedKeys[i - 2]:
13                dp[i] += dp[i - 2]
14
15            if i >= 3 and pressedKeys[i - 1] == pressedKeys[i - 2] == pressedKeys[i - 3]:
16                dp[i] += dp[i - 3]
17
18            if (
19                pressedKeys[i - 1] in "79"
20                and i >= 4
21                and pressedKeys[i - 1] == pressedKeys[i - 2]
22                == pressedKeys[i - 3] == pressedKeys[i - 4]
23            ):
24                dp[i] += dp[i - 4]
25
26            dp[i] %= MOD
27
28        return dp[n]