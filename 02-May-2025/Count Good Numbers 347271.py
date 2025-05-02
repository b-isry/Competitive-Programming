# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = (10 ** 9 ) + 7

        def power(base, exp):
            if exp == 0:
                return 1
            
            res = power(base, exp // 2)
            res *= res
            res %= MOD
            if exp%2: res *= base
            res %= MOD

            return res
        return (power(5, (n+1)//2)) * (power(4, (n)//2))%MOD




        