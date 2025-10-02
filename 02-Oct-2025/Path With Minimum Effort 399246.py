# Problem: Path With Minimum Effort - https://leetcode.com/problems/path-with-minimum-effort/description/

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap = [(0, 0, 0)]
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        row, col = len(heights), len(heights[0])

        while heap:
            effort, r, c = heapq.heappop(heap)

            if (r, c) == (row - 1, col - 1):
                return effort
            
            if (r, c) in visited:
                continue
            
            visited.add((r, c))


            for cr, cc in directions:
                nr, nc = cr + r, cc + c

                if (nr in range(row) and nc in range(col)) and (nr, nc) not in visited:
                    heapq.heappush(heap, (max(abs(heights[r][c] - heights[nr][nc]), effort), nr, nc))
