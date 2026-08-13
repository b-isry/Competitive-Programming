# Last updated: 8/13/2026, 2:29:31 PM
1class Solution:
2    def minOperations(self, nums: List[int]) -> int:
3        operation_cnt = Counter(nums)
4        cnt = 0
5
6        for i, n in operation_cnt.items():
7            if n == 1:
8                return -1
9            cnt += (n + 2) // 3
10
11        return cnt