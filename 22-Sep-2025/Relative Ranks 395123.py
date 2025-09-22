# Problem: Relative Ranks - https://leetcode.com/problems/relative-ranks/description/

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = [(-s, i) for i, s in enumerate(score)]
        heapq.heapify(heap)

        res = [""] * len(score)
        rank = 1
        while heap:
            _, i = heapq.heappop(heap)
            if rank == 1:
                res[i] = "Gold Medal"
            elif rank == 2:
                res[i] = "Silver Medal"
            elif rank == 3:
                res[i] = "Bronze Medal"
            else:
                res[i] = str(rank)
            rank += 1

        return res