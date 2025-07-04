# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        queue = deque()
        fresh = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        minute = -1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dx, dy in directions:
                    nr = r + dx
                    nc = c + dy

                    if (0 <= nr < row and 0 <= nc < col) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1
            minute += 1

        return minute if fresh == 0 else -1
