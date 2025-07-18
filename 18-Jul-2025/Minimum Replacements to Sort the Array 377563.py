# Problem: Minimum Replacements to Sort the Array - https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        cnt = 0
        max_ = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > max_:
                n = math.ceil(nums[i] / max_)
                cnt += n - 1
                max_ = nums[i] // n
            else:
                max_ = nums[i]
        return cnt