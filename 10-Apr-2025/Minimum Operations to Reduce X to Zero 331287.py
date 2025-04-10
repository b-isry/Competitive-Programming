# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        target = sum(nums) - x
        t = 0
        max_win = -1
        left, right = 0, 0
        
        for right in range(n):  
            t += nums[right]

            while t > target and left <= right:
                t -= nums[left]
                left += 1

            if t == target:
                max_win = max(max_win, right - left + 1)
                
        return -1 if max_win == -1 else n - max_win 

