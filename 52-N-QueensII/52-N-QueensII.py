# Last updated: 10/29/2026, 10:02:53 PM
1class Solution:
2    def totalNQueens(self, n: int) -> int:
3        cols = set()
4        diag1 = set()  
5        diag2 = set()  
6
7        def backtrack(row):
8            if row == n:
9                return 1
10
11            count = 0
12
13            for col in range(n):
14                if (col in cols or
15                    row - col in diag1 or
16                    row + col in diag2):
17                    continue
18
19                cols.add(col)
20                diag1.add(row - col)
21                diag2.add(row + col)
22
23                count += backtrack(row + 1)
24
25                cols.remove(col)
26                diag1.remove(row - col)
27                diag2.remove(row + col)
28
29            return count
30
31        return backtrack(0)