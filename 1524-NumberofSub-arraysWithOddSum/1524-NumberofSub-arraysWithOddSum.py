# Last updated: 11/15/2026, 9:37:08 PM
1class Solution:
2    def numOfSubarrays(self, arr: list[int]) -> int:
3        MOD = 10**9 + 7
4
5        even = 1
6        odd = 0
7        prefix = 0
8        result = 0
9
10        for num in arr:
11            prefix += num
12
13            if prefix % 2 == 0:
14                result += odd
15                even += 1
16            else:
17                result += even
18                odd += 1
19
20        return result % MOD
21