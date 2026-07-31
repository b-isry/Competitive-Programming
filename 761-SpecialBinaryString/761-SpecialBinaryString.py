# Last updated: 7/31/2026, 9:21:43 PM
1class Solution:
2    def makeLargestSpecial(self, s: str) -> str:
3        parts = []
4        bal = 0
5        start = 0
6
7        for i, ch in enumerate(s):
8            bal += 1 if ch == '1' else -1
9
10            if bal == 0:
11                parts.append(
12                    "1" +
13                    self.makeLargestSpecial(s[start + 1:i]) +
14                    "0"
15                )
16                start = i + 1
17
18        parts.sort(reverse=True)
19        return ''.join(parts)