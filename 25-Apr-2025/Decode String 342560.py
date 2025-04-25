# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        k = 0
        curr = ""
        for i in s:
            if i.isdigit():
                k = k * 10 + int(i)
            elif i == "[":
                stack.append((curr, k))
                curr = ""
                k = 0
            elif i == "]":
                prev, n = stack.pop()
                curr = prev + curr * n
            else:
                curr += i
        return curr

