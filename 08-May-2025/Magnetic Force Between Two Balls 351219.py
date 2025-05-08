# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left, right = 1, position[-1] - position[0]
        res = 0
        
        while left <= right:
            mid = (left + right) // 2
            count = 1
            last = position[0]
            for p in position[1:]:
                if p - last >= mid:
                    count += 1
                    last = p
                    if count >= m:
                        break
            if count >= m:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res