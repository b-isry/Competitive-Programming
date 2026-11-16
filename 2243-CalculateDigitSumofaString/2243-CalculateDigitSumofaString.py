# Last updated: 11/16/2026, 9:19:15 PM
1class Solution:
2    def digitSum(self, s: str, k: int) -> str:
3        while len(s) > k:
4            result = []
5
6            for i in range(0, len(s), k):
7                group = s[i:i + k]
8                total = sum(int(digit) for digit in group)
9                result.append(str(total))
10
11            s = "".join(result)
12
13        return s