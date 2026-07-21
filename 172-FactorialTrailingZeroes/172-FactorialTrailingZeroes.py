# Last updated: 7/22/2026, 12:50:11 AM
1class Solution:
2    def trailingZeroes(self, n: int) -> int:
3        ans = 0
4
5        while n:
6            n //= 5
7            ans += n
8
9        return ans