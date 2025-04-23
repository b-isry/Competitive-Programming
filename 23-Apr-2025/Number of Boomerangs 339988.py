# Problem: Number of Boomerangs - https://leetcode.com/problems/number-of-boomerangs/description/

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        cnt = 0
        for p in points:
            d = {}
            for q in points:
                distance = (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
                d[distance] = d.get(distance, 0) + 1
            for k in d:
                cnt += d[k] * (d[k] - 1)
        return cnt