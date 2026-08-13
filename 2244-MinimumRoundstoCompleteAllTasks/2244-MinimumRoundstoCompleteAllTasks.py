# Last updated: 8/13/2026, 2:30:58 PM
1class Solution:
2    def minimumRounds(self, tasks: List[int]) -> int:
3        task_cnt = Counter(tasks)
4        cnt = 0
5
6        for i, n in task_cnt.items():
7            if n == 1:
8                return -1
9            cnt += (n + 2) // 3
10
11        return cnt