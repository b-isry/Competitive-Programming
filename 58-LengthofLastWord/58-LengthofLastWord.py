# Last updated: 8/15/2026, 9:43:05 PM
1class Solution:
2    def lengthOfLastWord(self, s: str) -> int:
3        return len(s.strip().split()[-1])