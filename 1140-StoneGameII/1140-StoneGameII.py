# Last updated: 8/9/2026, 9:11:03 PM
1class Solution:
2    def arrayRankTransform(self, arr: List[int]) -> List[int]:
3        sorted_arr = sorted(set(arr))
4
5        rank = {}
6        for i, num in enumerate(sorted_arr):
7            rank[num] = i + 1
8
9        return [rank[num] for num in arr]