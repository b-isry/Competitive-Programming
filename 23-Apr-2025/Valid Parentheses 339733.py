# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'[' : ']', '{' : '}', '(' : ')'}
        for i in range(len(s)):
            if s[i] in brackets.keys():
                stack.append(s[i])
            else:
                if not stack:
                    return False
                a = stack.pop()
                if s[i] != brackets[a]:
                    return False
        return stack == []

        