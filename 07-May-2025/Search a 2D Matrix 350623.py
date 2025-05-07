# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = [i for row in matrix for i in row]
        l , r = 0 , len(nums)-1
        while l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
        