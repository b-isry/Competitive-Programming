# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        nums = [i for mat in matrix for i in mat]
        heapq.heapify(nums)
        for _ in range(k - 1):
            heapq.heappop(nums)
        return heapq.heappop(nums)