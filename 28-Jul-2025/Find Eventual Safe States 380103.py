# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        g = [[] for _ in range(n)]
        indeg = [0]*n
        res = []

        for i in range(n):
            for j in graph[i]:
                g[j].append(i)
                indeg[i] += 1
        q=deque(i for i in range(n) if indeg[i]==0)

        while q:
            node = q.popleft()
            res.append(node)
            for nei in g[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        res.sort()
        return res


        

