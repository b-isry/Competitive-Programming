# Problem: The kth Factor of n - https://leetcode.com/problems/the-kth-factor-of-n/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        cnt = 0
        for i in range(1, n + 1):
            if n % i == 0:
                cnt += 1
                if k == cnt:
                    return i
        if cnt < k:
            return -1
