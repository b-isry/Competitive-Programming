# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n+1)}
        for u, v, w in times:
            graph[u].append((v, w))

        def dijkstra(graph, start):
            min_time = {node: float('inf') for node in graph}
            min_time[start] = 0
            pq = [(0, start)]

            while pq:
                curr, node = heapq.heappop(pq)
                if curr > min_time[node]:
                    continue
                for neighbor, weight in graph[node]:
                    new_time = curr + weight
                    if new_time < min_time[neighbor]:
                        min_time[neighbor] = new_time
                        heapq.heappush(pq, (new_time, neighbor))
            return min_time

        t = dijkstra(graph, k)
        res = max(t.values())
        return res if res != float('inf') else -1