# Problem: Distinct Prime Factors of Product of Array - https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def factorize(n: int) -> list[int]:
            factorization: list[int] = []
            d = 2
            while d * d <= n:
                while n % d == 0:
                    factorization.append(d)
                    n //= d
                d += 1  
            if n > 1:
                factorization.append(n)
            return factorization
        
        primes = set()
        for x in nums:
            for p in factorize(x):
                primes.add(p)

        ans = len(primes)
        return ans

