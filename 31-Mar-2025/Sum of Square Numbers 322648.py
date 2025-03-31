# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # nums = list(range(c + 1))
        i , j = 0, int(sqrt(c))
        
        while i <= c and j >= 0:
            curr_sum = (i * i) + (j * j)
            if curr_sum == c:
                return True
            elif curr_sum < c:
                i += 1
            else:
                j -= 1

        return False
        