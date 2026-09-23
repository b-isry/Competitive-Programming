# Last updated: 9/23/2026, 10:37:56 PM
1class Solution:
2    def reverseWords(self, s: str) -> str:
3        s = list(s.split())
4        s.reverse()
5    
6        return " ".join(s)