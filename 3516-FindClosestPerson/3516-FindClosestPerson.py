# Last updated: 6/12/2026, 4:06:19 PM
1class Solution:
2    def findClosest(self, x: int, y: int, z: int) -> int:
3        if abs(z - x) < abs(z - y):
4            return 1
5        elif abs(z - x) > abs(z - y):
6            return 2
7        else:
8            return 0