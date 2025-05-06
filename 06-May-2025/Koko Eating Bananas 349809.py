# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:        
        r = sum(piles)
        l = 1
        res = r

        while l <= r:
            m = (l+r)//2
            i = 0

            for n in piles:
                i += ceil(n/m)
                
            if i > h:
                l = m+1
            else:
                res = min(res, m)
                r = m-1
        
        return res

