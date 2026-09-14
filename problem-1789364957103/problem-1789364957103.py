# Last updated: 9/14/2026, 8:49:17 AM
1class Solution:
2    def maxScoreIndices(self, nums: List[int]) -> List[int]:
3        ones = nums.count(1)
4        zeros = 0
5        ans = [zeros + ones]
6        for i in nums:
7            if i == 0:
8                zeros += 1
9            else:
10                ones -= 1
11            ans.append(zeros + ones)
12        max_score = max(ans)
13        return [i for i, val in enumerate(ans) if val == max_score]
14