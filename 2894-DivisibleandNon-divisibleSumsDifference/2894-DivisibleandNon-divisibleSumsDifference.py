# Last updated: 8/19/2026, 10:39:29 PM
1class Solution:
2    def differenceOfSums(self, n: int, m: int) -> int:
3        num1 = 0
4        num2 = 0
5
6        for i in range(1, n+1):
7            if i%m != 0:
8                num1 += i
9        
10        for i in range(1, n+1):
11            if i%m == 0:
12                num2 += i
13        
14        return num1 - num2