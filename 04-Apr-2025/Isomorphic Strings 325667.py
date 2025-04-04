# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        iso_map_s = {}
        iso_map_t = {}
        n = len(s)

        for i in range(n):
            if s[i] in iso_map_s:
                if iso_map_s[s[i]] != t[i]:
                    return False
            iso_map_s[s[i]] = t[i]

            if t[i] in iso_map_t:
                if iso_map_t[t[i]] != s[i]:
                    return False
            iso_map_t[t[i]] = s[i]

        return True 