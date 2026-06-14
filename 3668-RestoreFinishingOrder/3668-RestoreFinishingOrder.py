# Last updated: 6/14/2026, 2:45:37 PM
1class Solution:
2    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
3        ans = []
4
5        for person in order:
6            if person in friends:
7                ans.append(person)
8
9        return ans