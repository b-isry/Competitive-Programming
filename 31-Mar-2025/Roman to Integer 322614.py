# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_val = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        n = len(s)
        ans = 0
        i = 0
        while i < n:
            char = s[i]

            if i < n - 1 and roman_val[char] < roman_val[s[i + 1]]:
                ans += (roman_val[s[i + 1]] - roman_val[char])
                i += 1
            else:
                ans += roman_val[char]
            i += 1

        return ans
        