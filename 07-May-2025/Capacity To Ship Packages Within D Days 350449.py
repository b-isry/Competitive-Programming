# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l , r = max(weights), sum(weights)
        res = r

        while l <= r:
            mid = (l + r) // 2
            cap = 0
            ship = 1
            for w in weights:
                if cap + w > mid:
                    ship += 1
                    cap = 0
                cap += w
            if ship <= days:
                r = mid - 1
            else:
                l = mid + 1
        return l

        