# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(1 << len(nums)):
            curr = []
            for j in range(len(nums)):
                if i & (1 << j):
                    curr.append(nums[j])
            ans.append(curr)
        return ans