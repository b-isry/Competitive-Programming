# Last updated: 9/2/2026, 10:43:02 AM
1class Solution:
2    def alternatingSum(self, nums: List[int]) -> int:
3        ans = 0
4        n = len(nums)
5        for i in range(n):
6            if i % 2 == 0:
7                ans += nums[i]
8            else:
9                ans -= nums[i]
10        return ans