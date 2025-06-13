# Problem: Permutations II - https://leetcode.com/problems/permutations-ii/description/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        seen = set()

        def solve(path):
            if len(path) == len(nums):
                res.add(tuple(path))
                return
            for i in range(len(nums)):
                if i not in seen:
                    seen.add(i)
                    path.append(nums[i])
                    solve(path)
                    seen.remove(i)
                    path.pop()
        solve([])
        return list(res)
