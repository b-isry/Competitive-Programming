# Last updated: 8/14/2026, 9:15:17 PM
1class Solution:
2    def hIndex(self, citations: List[int]) -> int:
3        citations.sort(reverse=True)
4
5        h = 0
6
7        for i, cnt in enumerate(citations):
8            if cnt >= i + 1:
9                h = i + 1
10            else:
11                break
12
13        return h 