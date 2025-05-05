# Problem: K-th Symbol in Grammar - https://leetcode.com/problems/k-th-symbol-in-grammar/description/

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        isodd = (k % 2 == 1)
        prev = self.kthGrammar(n-1, (k+1)//2)
        if prev == 1:
            return 1 if isodd else 0
        elif prev == 0:
            return 0 if isodd else 1
