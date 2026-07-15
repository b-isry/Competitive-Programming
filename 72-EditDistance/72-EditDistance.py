# Last updated: 7/15/2026, 9:28:30 PM
1class Solution:
2    def minDistance(self, word1: str, word2: str) -> int:
3        m, n = len(word1), len(word2)
4
5        dp = [[0] * (n + 1) for _ in range(m + 1)]
6
7        for i in range(m + 1):
8            dp[i][0] = i
9
10        for j in range(n + 1):
11            dp[0][j] = j
12
13        for i in range(1, m + 1):
14            for j in range(1, n + 1):
15                if word1[i - 1] == word2[j - 1]:
16                    dp[i][j] = dp[i - 1][j - 1]
17                else:
18                    dp[i][j] = 1 + min(
19                        dp[i - 1][j],     
20                        dp[i][j - 1],      
21                        dp[i - 1][j - 1]   
22                    )
23
24        return dp[m][n]