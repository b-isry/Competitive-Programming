# Last updated: 8/16/2026, 10:06:03 PM
1class Solution:
2    def maxProduct(self, n: int) -> int:
3        digits = list(map(int, str(n)))
4        digits.sort(reverse = True)
5        return digits[0] * digits[1]
6