# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        cnt = 0
        for i in s:
            if i == "(":
                stack.append(cnt)
                cnt = 0
            else:
                cnt = stack.pop() + max(2*cnt, 1)
        
        return cnt
        


        