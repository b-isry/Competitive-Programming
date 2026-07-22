# Last updated: 7/22/2026, 9:52:54 PM
1class Solution:
2    def minimumTotal(self, triangle: List[List[int]]) -> int:
3        dp = triangle[-1][:]
4
5        for row in range(len(triangle) - 2, -1, -1):
6            for col in range(len(triangle[row])):
7                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])
8
9        return dp[0]