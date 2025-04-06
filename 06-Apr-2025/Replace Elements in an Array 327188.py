# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        n = len(nums)
        m = len(operations)
        nums_map = defaultdict()
        for i in range(n):
            nums_map[nums[i]] = i

        for i in range(m):
            if operations[i][0] in nums_map:
                j = nums_map[operations[i][0]]
                nums[j] = operations[i][1]
                nums_map[nums[j]] = nums_map[operations[i][0]]
        return nums
        