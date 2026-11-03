# Last updated: 11/3/2026, 9:30:49 PM
1class Solution:
2    def minMoves(self, nums: List[int]) -> int:
3        x = 0
4        y = max(nums)
5        for i in nums:
6            x += abs(y-i)
7        
8        return x