# Last updated: 9/22/2026, 10:19:55 PM
1class Solution:
2    def missingMultiple(self, nums: List[int], k: int) -> int:
3        nums_set = set(nums)
4
5        mlt = k
6
7        while mlt in nums_set:
8            mlt += k
9
10        return mlt