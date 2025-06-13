# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        freq = defaultdict(int)
        for i, j in edges:
            freq[i] += 1
            freq[j] += 1

            if freq[i] > 1:
                return i
            elif freq[j] > 1:
                return j