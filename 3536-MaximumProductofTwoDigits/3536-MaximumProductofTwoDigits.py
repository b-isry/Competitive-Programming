# Last updated: 8/16/2026, 10:04:42 PM
1class Solution:
2    def maxProduct(self, n: int) -> int:
3        digits = list(map(int, str(n)))
4
5        max_prod = 0
6
7        for i in range(len(digits)):
8            for j in range(i + 1, len(digits)):
9                prod = digits[i] * digits[j]
10                max_prod = max(max_prod, prod)
11
12        return max_prod