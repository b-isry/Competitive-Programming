# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0
        rows, cols = len(grid) , len(grid[0])

        def inbound(row, col):
            return (0 <= row < rows and 0 <= col < cols)

        def bfs(row, col):
            q = deque()
            q.append((row, col))
            visited.add((row, col))

            while q:
                r, c = q.popleft()   

                di = {(0, 1), (0, -1), (1, 0), (-1, 0)}
                for dr, dc in di:
                    nr, nc = r + dr, c + dc
                    if inbound(nr, nc) and grid[nr][nc] == "1" and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        return islands


