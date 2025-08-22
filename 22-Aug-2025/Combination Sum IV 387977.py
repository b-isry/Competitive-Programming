# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {0:1}
        for ans in range(1, target+1):
            dp[ans] = 0
            for i in nums:
                dp[ans] += dp.get(ans-i, 0)
        return dp[target]