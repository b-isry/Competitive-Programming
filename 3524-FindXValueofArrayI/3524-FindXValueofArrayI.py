# Last updated: 9/21/2026, 10:57:02 PM
1class Solution:
2    def resultArray(self, nums: List[int], k: int) -> List[int]:
3        ans = [0] * k
4        dp = [0] * k
5
6        for num in nums:
7            new_dp = [0] * k
8
9            for r in range(k):
10                new_r = (r * num) % k
11                new_dp[new_r] += dp[r]
12            new_dp[num % k] += 1
13            for r in range(k):
14                ans[r] += new_dp[r]
15
16            dp = new_dp
17
18        return ans