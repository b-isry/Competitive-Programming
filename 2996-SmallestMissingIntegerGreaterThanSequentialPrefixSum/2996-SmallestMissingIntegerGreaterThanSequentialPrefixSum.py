# Last updated: 8/11/2026, 8:43:21 PM
1class Solution:
2    def missingInteger(self, nums: List[int]) -> int:
3        n = len(nums)
4        s = nums[0]
5
6        for a, b in pairwise(nums):
7            if b == a + 1:
8                s += b
9            else:
10                break
11
12        num_set = set(nums)
13
14        while s in num_set:
15            s+=1
16        return s
17
18