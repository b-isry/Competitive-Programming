# Problem: Find All Anagrams in a String - https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        p_cnt = Counter(p)
        l, r = 0, len(p)
        res = []

        while r < n + 1:
            if Counter(s[l:r]) == p_cnt:
                res.append(l)
            l += 1
            r += 1

        return res