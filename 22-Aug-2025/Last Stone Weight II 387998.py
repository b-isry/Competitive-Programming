# Problem: Last Stone Weight II - https://leetcode.com/problems/last-stone-weight-ii/description/

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stone_sum = sum(stones)
        target = ceil(stone_sum / 2)

        def dfs(i, total):
            if total >= target or i == len(stones):
                return abs(total - (stone_sum - total))
            if (i, total) in dp:
                return dp[(i,total)]
            
            dp[(i,total)] = min(dfs(i+1, total), dfs(i+1, total + stones[i]))
            return dp[(i, total)]
        
        dp = {}
        return dfs(0,0)