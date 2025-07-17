# Problem: Largest Odd Number in String - https://leetcode.com/problems/largest-odd-number-in-string/

class Solution:
    def largestOddNumber(self, num: str) -> str:
        nums = list(map(int, str(num)))
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] % 2 != 0:
                return "".join(map(str, nums[:i+1]))
        return ""

        