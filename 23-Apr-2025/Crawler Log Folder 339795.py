# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for i in logs:
            if i == "../" and len(stack) > 0:
                stack.pop()
            elif i != "../" and i != "./":
                stack.append(i)
                
        return len(stack)

