# Last updated: 9/7/2026, 7:03:04 PM
1class Solution:
2    def maximumLengthSubstring(self, s: str) -> int:
3        cnt = {}
4        l = 0
5        ans = 0
6        for r in range(len(s)):
7            cnt[s[r]] = cnt.get(s[r], 0) + 1
8
9            while cnt[s[r]] > 2:
10                cnt[s[l]] -= 1
11                l += 1
12            
13            ans = max(ans, r-l+1)
14        
15        return ans