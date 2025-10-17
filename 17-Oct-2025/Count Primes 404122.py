# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        
        i = 2
        while i * i < n:
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False
            i += 1
        
        return sum(is_prime)