# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        answer = [0] * n
        stack = []

        for i in range(n):
            while stack and temp[stack[-1]] < temp[i]:
                p = stack.pop()
                answer[p] = i - p
            stack.append(i)
        
        return answer