# Problem: Find the Smallest Divisor Given a Threshold - https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
            
        while l <= r:
            mid = (l + r) // 2
            total = 0
            for i in nums:
                total += ceil(i / mid)
            
            if total > threshold:
                l = mid + 1
            else:
                r = mid - 1
        return l