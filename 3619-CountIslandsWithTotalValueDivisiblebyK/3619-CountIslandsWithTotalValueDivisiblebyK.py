# Last updated: 10/26/2026, 8:51:43 PM
1class Solution:
2    def countIslands(self, grid: List[List[int]], k: int) -> int:
3        m, n = len(grid), len(grid[0])
4        count = 0
5
6        def dfs(r, c):
7            if r < 0 or r >= m or c < 0 or c >= n:
8                return 0
9
10            if grid[r][c] == 0:
11                return 0
12
13            value = grid[r][c]
14            grid[r][c] = 0 
15
16            value += dfs(r + 1, c)
17            value += dfs(r - 1, c)
18            value += dfs(r, c + 1)
19            value += dfs(r, c - 1)
20
21            return value
22
23        for r in range(m):
24            for c in range(n):
25                if grid[r][c] > 0:
26                    total = dfs(r, c)
27
28                    if total % k == 0:
29                        count += 1
30
31        return count
32