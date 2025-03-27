# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_cnt = 0
        result = [0,0]
        for row in range(len(mat)):
            cnt = 0
            for col in range(len(mat[row])):
                if mat[row][col] == 1:
                    cnt += 1
            if cnt > result[1]:
                result[0] = row
                result[1] = cnt

        return result
            
        