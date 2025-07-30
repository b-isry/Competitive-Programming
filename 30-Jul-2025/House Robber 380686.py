# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [0]*n

        for i in range(n):
            if i == 0 or i == 1:
                memo[i] = max(nums[i], nums[0])
            else:
                memo[i] = max(memo[i-1], memo[i-2] + nums[i])
        return memo[n-1]