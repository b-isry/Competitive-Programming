# Last updated: 9/25/2026, 12:02:32 AM
1class Solution:
2    def increasingTriplet(self, nums: list[int]) -> bool:
3        first = float("inf")
4        second = float("inf")
5
6        for num in nums:
7            if num <= first:
8                first = num
9            elif num <= second:
10                second = num
11            else:
12                return True
13
14        return False