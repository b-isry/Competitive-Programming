# Problem: Prime Palindrome - https://leetcode.com/problems/prime-palindrome/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(x):
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            i = 3
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 2
            return True

        def is_palindrome(x):
            return str(x) == str(x)[::-1]

        while True:
            if is_palindrome(n) and is_prime(n):
                return n
            n += 1

            if 10**7 < n < 10**8:
                n = 10**8