# Last updated: 8/20/2026, 11:33:08 PM
1class Solution:
2    def resultArray(self, nums: List[int]) -> List[int]:
3        nums1 = [nums[0]]
4        nums2 = [nums[1]]
5        for i in nums[2:]:
6            if nums1[len(nums1)-1] > nums2[len(nums2)-1]:
7                nums1.append(i)
8            else:
9                nums2.append(i)
10        return nums1 + nums2
11
12
13