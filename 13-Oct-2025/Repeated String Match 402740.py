# Problem: Repeated String Match - https://leetcode.com/problems/repeated-string-match/description/

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        rep = -(-len(b) // len(a))
        for k in [rep, rep + 1]:
            if b in a * k:
                return k
        return -1