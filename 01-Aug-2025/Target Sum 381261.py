# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(i, curr):
            if i == len(nums):
                return 1 if curr == target else 0
            if (i, curr) in memo:
                return memo[i, curr]
            
            memo[(i, curr)] = (dp(i+1, curr + nums[i]) + dp(i+1, curr - nums[i]))
            return memo[(i, curr)]
        return dp(0, 0)