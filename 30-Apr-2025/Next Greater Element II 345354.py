# Problem: Next Greater Element II - https://leetcode.com/problems/next-greater-element-ii/

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        ans = [-1] * n

        for i in range(n*2, -1, -1):
            while stack and stack[-1] <= nums[i%n]:
                stack.pop()
            if i < n:
                ans[i] = -1 if not stack else stack[-1]
            stack.append(nums[i%n])
        return ans

