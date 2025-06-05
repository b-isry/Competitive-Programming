# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(curr, op, cp):
            if len(curr) == 2 * n:
                res.append(curr)
                return
            if op < n:
                backtrack(curr + "(", op + 1, cp)
            if cp < op:
                backtrack(curr + ")", op, cp + 1)
            
        backtrack("",0,0)
        return res
