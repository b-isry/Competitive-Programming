# Last updated: 8/14/2026, 9:19:06 PM
1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3        k = 0
4
5        for i in range(len(nums)):
6            if nums[i] != val:
7                nums[k] = nums[i]
8                k += 1
9
10        return k