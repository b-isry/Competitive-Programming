# Last updated: 8/28/2026, 11:31:16 PM
1class Solution:
2    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
3        total = 0
4
5        for i in range(len(timeSeries) - 1):
6            total += min(duration, timeSeries[i + 1] - timeSeries[i])
7
8        total += duration
9
10        return total