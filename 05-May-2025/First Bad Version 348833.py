# Problem: First Bad Version - https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        def helper(l, r):
            if l == r:
                return l
            mid = (l+r) // 2
            if isBadVersion(mid):
                return helper(l, mid)
            else:
                return helper(mid+1, r)
        
        return helper(1, n)