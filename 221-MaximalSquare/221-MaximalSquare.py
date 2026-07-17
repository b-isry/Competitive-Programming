# Last updated: 7/17/2026, 10:33:43 PM
1class Solution:
2    def maximalSquare(self, matrix: List[List[str]]) -> int:
3        m, n = len(matrix), len(matrix[0])
4
5        dp = [[0] * n for _ in range(m)]
6        max_side = 0
7
8        for i in range(m):
9            for j in range(n):
10                if matrix[i][j] == "1":
11                    if i == 0 or j == 0:
12                        dp[i][j] = 1
13                    else:
14                        dp[i][j] = 1 + min(
15                            dp[i - 1][j],
16                            dp[i][j - 1],
17                            dp[i - 1][j - 1]
18                        )
19
20                    max_side = max(max_side, dp[i][j])
21
22        return max_side * max_side