# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        idx = []
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    idx.append((i,j))
            print(idx)

        for i, j in idx:
            for k in range(cols):
                matrix[i][k] = 0
            for k in range(rows):
                matrix[k][j] = 0


                    

        