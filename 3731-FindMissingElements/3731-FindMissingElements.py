# Last updated: 8/4/2026, 8:29:24 PM
1class Solution:
2    def findMissingElements(self, nums: List[int]) -> List[int]:
3        j = max(nums)
4        i = min(nums)
5        ans = []
6        for n in range(i, j):
7            if n not in nums:
8                ans.append(n)
9        return ans
10