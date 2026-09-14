# Last updated: 9/14/2026, 8:23:00 AM
1class Solution:
2    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
3        max_candy = max(candies)
4        ans = []
5        for i in candies :
6            if i + extraCandies >= max_candy:
7                ans.append(True)
8            else:
9                ans.append(False)
10        return ans
11