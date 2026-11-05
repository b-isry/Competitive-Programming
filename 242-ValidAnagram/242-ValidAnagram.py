# Last updated: 11/6/2026, 2:33:16 AM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        return Counter(s) == Counter(t)