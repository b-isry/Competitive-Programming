# Last updated: 8/10/2026, 10:22:16 PM
1class Solution:
2    def angleClock(self, hour: int, minutes: int) -> float:
3        hr = hour * 30 + minutes * 0.5
4        mi = minutes * 6
5        ans = abs(hr - mi)
6
7        return min(ans, abs(360 - ans))