# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        comb = []
        def backtrack(start, remaining):
            if remaining == 0:
                res.append(comb.copy())
                return
            for i in range(start, len(candidates)):
                c = candidates[i]
                if c > remaining:
                    break
                comb.append(c)
                backtrack(i, remaining - c)
                comb.pop()
        backtrack(0, target)
        return res