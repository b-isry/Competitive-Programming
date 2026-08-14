# Last updated: 8/14/2026, 8:55:09 PM
1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        """
4        Do not return anything, modify nums1 in-place instead.
5        """
6        for i in nums2:
7            nums1[m] = i
8            m += 1
9        
10        nums1.sort()