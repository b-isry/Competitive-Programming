# Last updated: 9/23/2026, 10:49:22 PM
1class Solution:
2    def productExceptSelf(self, nums: list[int]) -> list[int]:
3        total = 1
4        zero_count = nums.count(0)
5
6        for i in nums:
7            if i != 0:
8                total *= i
9
10        ans = []
11
12        for i in nums:
13            if zero_count > 1:
14                ans.append(0)
15            elif zero_count == 1:
16                if i == 0:
17                    ans.append(total)
18                else:
19                    ans.append(0)
20            else:
21                ans.append(total // i)
22
23        return ans