# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        duplicate = []
        for i in nums:
            if i in seen:
                duplicate.append(i)
            else:
                seen.add(i)

        return duplicate
