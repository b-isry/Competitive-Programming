# Last updated: 10/26/2026, 6:21:13 AM
1class Solution:
2    def closedIsland(self, grid: list[list[int]]) -> int:
3        m, n = len(grid), len(grid[0])
4
5        def dfs(r, c):
6            if r < 0 or r >= m or c < 0 or c >= n:
7                return
8
9            if grid[r][c] == 1:
10                return
11
12            grid[r][c] = 1
13
14            dfs(r + 1, c)
15            dfs(r - 1, c)
16            dfs(r, c + 1)
17            dfs(r, c - 1)
18
19        for r in range(m):
20            dfs(r, 0)
21            dfs(r, n - 1)
22
23        for c in range(n):
24            dfs(0, c)
25            dfs(m - 1, c)
26
27        count = 0
28
29        for r in range(1, m - 1):
30            for c in range(1, n - 1):
31                if grid[r][c] == 0:
32                    count += 1
33                    dfs(r, c)
34
35        return count