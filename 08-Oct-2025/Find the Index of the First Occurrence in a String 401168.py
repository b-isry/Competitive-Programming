# Problem: Find the Index of the First Occurrence in a String - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m > n:
            return -1

        for i in range(n - m + 1):
            j = 0
            while j < m and haystack[i + j] == needle[j]:
                j += 1
            if j == m:
                return i
        return -1
