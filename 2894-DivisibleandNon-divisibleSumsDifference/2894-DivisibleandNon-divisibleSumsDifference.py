# Last updated: 8/19/2026, 10:40:34 PM
1class Solution:
2    def differenceOfSums(self, n: int, m: int) -> int:
3         return sum(x if x % m != 0 else -x for x in range(1, n + 1))