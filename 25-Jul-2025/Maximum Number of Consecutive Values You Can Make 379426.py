# Problem: Maximum Number of Consecutive Values You Can Make - https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/description/

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        ans = 0
        for i in coins:
            if i >= ans + 2:
                break
            ans += i
        return ans + 1