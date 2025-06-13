# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        res = []
        directed_to = set()
        for u,v in edges:
            directed_to.add(v)
        for i in range(n):
            if i not in directed_to:
                res.append(i)
        return res