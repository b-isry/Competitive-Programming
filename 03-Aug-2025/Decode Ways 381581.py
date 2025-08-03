# Problem: Decode Ways - https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:

        if not s or s[0] == '0':
            return 0
            
        n = len(s)
        memo = [0] * (n+1)
        memo[0] = memo[1] = 1

        for i in range(2, n+1):
            if 1 <= int(s[i-1:i]) <= 9:
                memo[i] += memo[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                memo[i] += memo[i-2]

        return memo[n]


        