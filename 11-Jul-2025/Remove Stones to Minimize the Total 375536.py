# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapq.heapify(piles)

        while k > 0:
            x = heapq.heappop(piles)
            x = ceil(-x / 2)
            heapq.heappush(piles, -x)
            k = k - 1
        total = sum(piles)
        return abs(total)