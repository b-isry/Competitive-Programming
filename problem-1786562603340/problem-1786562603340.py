# Last updated: 8/12/2026, 10:23:23 PM
1class Solution:
2    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
3        freq = {}
4        l = 0
5        ans = 0
6
7        for r in range(len(nums)):
8            freq[nums[r]] = freq.get(nums[r], 0) + 1
9
10            while freq[nums[r]] > k:
11                freq[nums[l]] -= 1
12                l += 1
13
14            ans = max(ans, r - l + 1)
15
16        return ans