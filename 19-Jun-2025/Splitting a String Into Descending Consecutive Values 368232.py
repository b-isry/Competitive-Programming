# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        def back(idx, parts, prev):
            if idx == n:
                return parts >= 2
            for i in range(idx, n):
                num = int(s[idx : i+1])
                if prev == math.inf or num == prev-1:
                    if back(i+1, parts + 1, num):
                        return True
            return False

        n = len(s)
        return back(0, 0, math.inf)
        