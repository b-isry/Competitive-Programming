# Last updated: 9/16/2026, 10:26:54 PM
1class Solution:
2    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
3        s = s1.split(" ") + s2.split(" ")
4        ans = []
5        cnt = Counter(s)
6        for ch, n in cnt.items():
7            if n == 1:
8                ans.append(ch)
9        return ans
10            
11        
12