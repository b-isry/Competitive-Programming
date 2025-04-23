# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')

        for i in path:
            if i == "..":
                if len(stack) > 0:
                    stack.pop()
            elif i != "." and i != "":
                stack.append(i)

        return "/" + "/".join(stack)
