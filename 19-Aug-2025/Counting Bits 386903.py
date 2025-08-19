# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            cnt = 0
            x = i
            while x:
                cnt += x & 1   
                x >>= 1        
            ans.append(cnt)
        return ans