# Last updated: 10/3/2026, 10:59:07 AM
1class Solution:
2    def generateParenthesis(self, n: int) -> list[str]:
3        result = []
4
5        def backtrack(curr, op, cl):
6            if len(curr) == 2 * n:
7                result.append(curr)
8                return
9
10            if op < n:
11                backtrack(curr + "(", op + 1, cl)
12
13            if cl < op:
14                backtrack(curr + ")", op, cl + 1)
15
16        backtrack("", 0, 0)
17        return result