# Last updated: 8/17/2026, 9:03:40 PM
1class Solution:
2    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
3        less = []
4        eq = []
5        gr = []
6
7        for num in nums:
8            if num < pivot:
9                less.append(num)
10            elif num == pivot:
11                eq.append(num)
12            else:
13                gr.append(num)
14
15        return less + eq + gr