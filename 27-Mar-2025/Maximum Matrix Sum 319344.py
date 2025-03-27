# Problem: Maximum Matrix Sum - https://leetcode.com/problems/maximum-matrix-sum/description/?envType=problem-list-v2&envId=matrix

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0 
        min_ans = float('inf')
        neg_cnt = 0
        for row in matrix:
            for col in row:
                min_ans = min(min_ans, abs(col))
                if col < 0:
                    total += abs(col)
                    neg_cnt += 1
                else:
                    total += col
        if neg_cnt % 2 != 0:
            return total - (2 * min_ans)
        
        return total

        