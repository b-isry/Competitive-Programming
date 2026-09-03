# Last updated: 9/3/2026, 6:54:26 PM
1class Solution:
2    def uniformArray(self, nums1: list[int]) -> bool:
3        min_odd = float('inf')
4        min_even = float('inf')
5
6        for x in nums1:
7            if x % 2:
8                min_odd = min(min_odd, x)
9            else:
10                min_even = min(min_even, x)
11
12        if min_odd == float('inf') or min_even == float('inf'):
13            return True
14
15        return min_odd < min_even