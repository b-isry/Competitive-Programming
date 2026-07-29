# Last updated: 7/29/2026, 10:08:03 PM
1class Solution:
2    def findLUSlength(self, a: str, b: str) -> int:
3        if a == b:
4            return -1
5        return max(len(a), len(b))