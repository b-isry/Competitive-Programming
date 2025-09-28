# Problem: Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn, mx = min(nums), max(nums)
        
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        
        return gcd(mn, mx)
