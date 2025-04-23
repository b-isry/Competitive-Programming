# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i != '+' and i != '/' and i != '-' and i != '*':
                stack.append(int(i))
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                if i == "+":
                    stack.append(n2 + n1)
                elif i == "-":
                    stack.append(n2 - n1)
                elif i == "*":
                    stack.append(n2 * n1)
                elif i == "/":
                    stack.append(int(n2 / n1))

        return stack[-1]



        