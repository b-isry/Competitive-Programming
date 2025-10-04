# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = {i: [] for i in range(n)}
        for (u, v), p in zip(edges, succProb):
            graph[u].append((v, p))
            graph[v].append((u, p))
        
        def dij(graph, start):
            max_prob = [0.0] * n
            max_prob[start] = 1.0
            pq = [(-1.0, start)]
            
            while pq:
                curr, node = heapq.heappop(pq)
                curr = -curr

                if curr > max_prob[node]:
                    continue

                for ng, p in graph[node]:
                    new = curr * p
                    if new > max_prob[ng]:
                        max_prob[ng] = new
                        heapq.heappush(pq, (-new, ng))

            return max_prob
        
        max_p = dij(graph, start_node)
        return max_p[end_node]
