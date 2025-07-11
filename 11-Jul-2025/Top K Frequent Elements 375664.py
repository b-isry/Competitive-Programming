# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        cnt = Counter(nums)

        for i, freq in cnt.items():
            heapq.heappush(ans, (freq, i))
            if len(ans) > k:
                heapq.heappop(ans)
        return [i for freq, i in ans]

