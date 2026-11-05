# Last updated: 11/6/2026, 2:25:57 AM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        return sorted(s) == sorted(t)