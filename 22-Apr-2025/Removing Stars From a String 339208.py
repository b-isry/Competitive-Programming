# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/description/

class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        for i in range(len(s)):
            if s[i] == "*":
                res.pop() 
            else:
                res.append(s[i])
        
        return "".join(res)