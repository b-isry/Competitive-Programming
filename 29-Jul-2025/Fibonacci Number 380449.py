# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        memo = defaultdict(int)
        if n == 1 or n == 0:
            return n
        if n not in memo:
            memo[n] = self.fib(n-2) + self.fib(n-1)
        return memo[n]
        