# Problem: Count Servers that Communicate - https://leetcode.com/problems/count-servers-that-communicate/description/

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        root = [i for i in range(m+n)]

        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                root[py] = px

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    union(i, m+j)

        cnt = [0] * (m+n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    r = find(i)
                    cnt[r] += 1

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    r = find(i)
                    if cnt[r] > 1:
                        ans += 1
        return ans
