# Problem: Three Divisors - https://leetcode.com/problems/three-divisors/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def isThree(self, n: int) -> bool:
        cnt = 0
        for i in range(2, n):
            if n % i == 0:
                cnt += 1

        return True if cnt == 1 else False

        