# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxDeque = deque()
        minDeque = deque()
        left = 0
        res = 0

        for right in range(len(nums)):
            while maxDeque and nums[right] > maxDeque[-1]:
                maxDeque.pop()
            while minDeque and nums[right] < minDeque[-1]:
                minDeque.pop()

            maxDeque.append(nums[right])
            minDeque.append(nums[right])

            while maxDeque[0] - minDeque[0] > limit:
                if maxDeque[0] == nums[left]:
                    maxDeque.popleft()
                if minDeque[0] == nums[left]:
                    minDeque.popleft()
                left += 1

            res = max(res, right - left + 1)

        return res