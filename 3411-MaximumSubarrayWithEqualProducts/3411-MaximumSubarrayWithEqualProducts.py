# Last updated: 11/25/2026, 2:48:44 AM
1class Solution:
2    def maxLength(self, nums: List[int]) -> int:
3        n = len(nums)
4        ans = 1
5
6        for left in range(n):
7            prod = 1
8            g = 0
9            l = 1
10
11            for right in range(left, n):
12                x = nums[right]
13                prod *= x
14                g = gcd(g, x)
15                l = l * x // gcd(l, x)
16
17                if prod == g * l:
18                    ans = max(ans, right - left + 1)
19
20        return ans