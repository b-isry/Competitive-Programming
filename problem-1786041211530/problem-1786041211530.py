# Last updated: 8/6/2026, 9:33:31 PM
1class Solution:
2    def smallestNumber(self, n: int, t: int) -> int:
3        for i in range(n, n+11):
4            x = math.prod(int(d) for d in str(i))
5            if x % t == 0:
6                return i