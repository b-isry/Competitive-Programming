# Last updated: 11/6/2026, 3:16:01 AM
1class Solution:
2    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
3        freq = Counter(nums)
4        return [num for num, _ in freq.most_common(k)]
5