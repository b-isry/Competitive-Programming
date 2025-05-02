# Problem: Asteroid Collision - https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i, val in enumerate(asteroids):
            skip = False
            while stack and stack[-1]>0 and val<0:
                if abs(stack[-1]) == abs(val):
                    stack.pop()
                    skip = True
                    break
                elif abs(stack[-1]) > abs(val):
                    skip = True
                    break
                else:
                    stack.pop()
            if not skip:
                stack.append(val)

        return stack