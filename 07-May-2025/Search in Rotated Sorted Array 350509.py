# Problem: Search in Rotated Sorted Array - https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left , right = 0 , len(nums)-1

        while left <= right:
            mid = (left + right)
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                if nums[left] > target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid] > target > nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1


        