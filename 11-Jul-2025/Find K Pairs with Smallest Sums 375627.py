# Problem: Find K Pairs with Smallest Sums - https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        seen = set()
        min_heap = []

        heapq.heappush(min_heap, (nums1[0] + nums2[0], 0, 0))
        seen.add((0,0))

        while min_heap and len(ans) < k:
            _sum, i, j = heapq.heappop(min_heap)
            ans.append([nums1[i], nums2[j]])

            if j+1 < len(nums2) and (i, j + 1) not in seen:
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
                seen.add((i, j+1))
            if i+1 < len(nums1) and (i + 1, j) not in seen:
                heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], i + 1, j))
                seen.add((i+1, j))
        return ans
