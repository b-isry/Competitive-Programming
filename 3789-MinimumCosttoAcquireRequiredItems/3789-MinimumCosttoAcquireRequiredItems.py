# Last updated: 11/11/2026, 9:39:12 PM
1class Solution:
2    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
3        s = need1 * cost1 + need2 * cost2
4
5        com = min(need1, need2) * costBoth
6        rem = abs(need1 - need2)
7
8        if need1 > need2:
9            com += rem * min(cost1, costBoth)
10        else:
11            com += rem * min(cost2, costBoth)
12
13        extra = max(need1, need2) * costBoth
14
15        return min(s, com, extra)