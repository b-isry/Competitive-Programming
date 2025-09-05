# Problem: Find the Difference - https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        cnt1 = Counter(s)
        cnt2 = Counter(t)

        for ch, i in cnt2.items():
            if ch not in cnt1 or i != cnt1[ch]:
                return ch
            

