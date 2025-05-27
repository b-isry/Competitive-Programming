# Problem: Intersection of Two Arrays II - https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        res = []

        for i in range(len(nums1)):
            l , r = 0, len(nums2)-1
            while l <= r:
                m = (l + r) // 2
                if nums2[m] == nums1[i]:
                    res.append(nums2.pop(m))
                    break
                elif nums2[m] < nums1[i]:
                    l = m + 1
                else:
                    r = m - 1
        return res