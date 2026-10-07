# Last updated: 10/7/2026, 9:55:37 PM
1class Solution:
2    def removeInvalidParentheses(self, s: str) -> list[str]:
3        def is_valid(s):
4            balance = 0
5
6            for c in s:
7                if c == '(':
8                    balance += 1
9                elif c == ')':
10                    balance -= 1
11
12                    if balance < 0:
13                        return False
14
15            return balance == 0
16
17        queue = deque([s])
18        visited = {s}
19        result = []
20
21        while queue:
22            found_valid = False
23
24            for _ in range(len(queue)):
25                current = queue.popleft()
26
27                if is_valid(current):
28                    result.append(current)
29                    found_valid = True
30                    continue
31
32                if found_valid:
33                    continue
34
35                for i in range(len(current)):
36                    if current[i] not in "()":
37                        continue
38
39                    if i > 0 and current[i] == current[i - 1]:
40                        continue
41
42                    next_string = current[:i] + current[i + 1:]
43
44                    if next_string not in visited:
45                        visited.add(next_string)
46                        queue.append(next_string)
47
48            if found_valid:
49                return result
50
51        return [""]