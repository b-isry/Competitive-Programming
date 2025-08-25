# Problem: 2 Keys Keyboard - https://leetcode.com/problems/2-keys-keyboard/description/

class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        ans = n
        for i in range(2, (n//2) + 1):
            if n % i == 0:
                ans = min(ans, i + self.minSteps(n // i))
        return ans