# Last updated: 10/5/2026, 10:27:20 PM
1class Solution:
2    def scoreOfParentheses(self, s: str) -> int:
3        stack = [0]
4
5        for char in s:
6            if char == "(":
7                stack.append(0)
8            else:
9                inner = stack.pop()
10
11                if inner == 0:
12                    score = 1
13                else:
14                    score = 2 * inner
15
16                stack[-1] += score
17
18        return stack[0]