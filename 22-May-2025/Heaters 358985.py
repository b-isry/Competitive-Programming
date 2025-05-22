# Problem: Heaters - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        n = len(heaters)
        rad = 0
        for h in houses:
            l, r = 0, n-1

            while l < r:
                m = (r + l) // 2

                if heaters[m] < h:
                    l = m + 1
                else:
                    r = m
            d = abs(heaters[l] - h)
            if l > 0:
                d = min(d, abs(heaters[l - 1] - h))
            rad = max(rad, d)
        return rad 