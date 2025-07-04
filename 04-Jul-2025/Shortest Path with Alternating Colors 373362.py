# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_graph = defaultdict(list)
        blue_graph = defaultdict(list)

        for u, v in redEdges:
            red_graph[u].append(v)
        
        for u, v in blueEdges:
            blue_graph[u].append(v)

        queue = deque()
        visited = set()

        queue.append((0, 0))
        queue.append((0, 1))
        visited.add((0, 0))
        visited.add((0, 1))

        output = [-1] * n
        level = 0

        while queue:
            for _ in range(len(queue)):
                curr_node, color = queue.popleft()

                if output[curr_node] == -1:
                    output[curr_node] = level

                next_color = 1 - color 
                next_graph = blue_graph if next_color == 1 else red_graph

                for neighbor in next_graph[curr_node]:
                    if (neighbor, next_color) not in visited:
                        visited.add((neighbor, next_color))
                        queue.append((neighbor, next_color))

            level += 1     

        return output