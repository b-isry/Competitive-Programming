# Problem: Clear Digits - https://leetcode.com/problems/clear-digits/description/

class Solution:
    def clearDigits(self, s: str) -> str:
        res = []
        for i in range(len(s)):
            if s[i].isalpha():
                res.append(s[i])
            elif s[i].isdigit():
                res.pop()
        
        return "".join(res)



